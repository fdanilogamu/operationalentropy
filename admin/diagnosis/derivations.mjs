const numeric = value => value !== '' && value != null && Number.isFinite(Number(value));
const mean = (records, key) => {
  const values = records.map(record => record[key]).filter(numeric).map(Number);
  return values.length ? values.reduce((sum, value) => sum + value, 0) / values.length : null;
};
const sum = (records, key) => records.map(record => record[key]).filter(numeric).reduce((total, value) => total + Number(value), 0);
const percent = (numerator, denominator) => denominator ? 100 * numerator / denominator : null;
const median = values => {
  const sorted = values.filter(numeric).map(Number).sort((a, b) => a - b);
  return sorted.length ? (sorted.length % 2 ? sorted[(sorted.length - 1) / 2] : (sorted[sorted.length / 2 - 1] + sorted[sorted.length / 2]) / 2) : null;
};

export function classificationRatio(records, field, positive, assessed) {
  const included = records.filter(record => assessed.includes(record[field]));
  return {value: percent(included.filter(record => record[field] === positive).length, included.length), numerator: included.filter(record => record[field] === positive).length, denominator: included.length};
}

export function deriveMetrics(state) {
  const s = state.samples;
  const founder = classificationRatio(s.criticalOperations, 'founderMemoryDependent', 'yes', ['yes', 'no']);
  const documents = classificationRatio(s.documents, 'obsolescenceStatus', 'materially_obsolete', ['current_usable', 'materially_obsolete']);
  const integrations = classificationRatio(s.integrations, 'outcome', 'successful', ['successful', 'failed']);
  const tools = classificationRatio(s.tools, 'classification', 'operational_deadweight', [
    'necessary_distinct', 'necessary_overlapping', 'useful_underutilized', 'specialized_low_frequency',
    'candidate_consolidation', 'operational_deadweight'
  ]);
  return {
    values: {
      decision_drag: sum(s.decisionEvents, 'blockedPersonHours') && state.engagement.sampledContributors && state.engagement.sampledWeeks ? sum(s.decisionEvents, 'blockedPersonHours') / Number(state.engagement.sampledContributors) / Number(state.engagement.sampledWeeks) : null,
      context_switching: state.engagement.qualifyingInterruptions && state.engagement.founderWorkdays ? Number(state.engagement.qualifyingInterruptions) / Number(state.engagement.founderWorkdays) : null,
      implicit_logic: founder.value,
      discoverability_gap: mean(s.retrievalTests, 'minutesElapsed'),
      obsolescence_rate: documents.value,
      onboarding_velocity: median(s.onboardingCases.map(record => record.actualDuration)),
      interruption_count: mean(s.projects, 'forcedStops'),
      rework_ratio: percent(sum(s.projects, 'avoidableReworkHours'), sum(s.projects, 'totalEffort')),
      alignment_drift: state.engagement.monthsSampled && s.projects.length ? sum(s.projects, 'realignmentEvents') / s.projects.length / Number(state.engagement.monthsSampled) : null,
      cognitive_load: state.engagement.toolContributors && state.engagement.toolWorkdays ? sum(s.toolWorkflows, 'avoidableMinutes') / Number(state.engagement.toolContributors) / Number(state.engagement.toolWorkdays) : null,
      integration_integrity: integrations.value,
      tool_utility: tools.value,
      context_loss: mean(s.handoffs.filter(record => numeric(record.contextLossRating) && Number(record.contextLossRating) >= 1 && Number(record.contextLossRating) <= 5), 'contextLossRating'),
      clarification_cycle_time: mean(s.handoffs, 'clarificationHours'),
      trust_in_handoff: mean(state.evidence.filter(record => !record.sourceInactive && String(record.metricIds || '').includes('trust_in_handoff')), 'quantitativeEstimate')
    },
    samples: {founder, documents, integrations, tools}
  };
}

export function validateToolRecord(record) {
  return ['candidate_consolidation', 'operational_deadweight', 'insufficient_evidence'].includes(record.classification) && !String(record.classificationReason || '').trim() ? ['Classification reason is required.'] : [];
}
