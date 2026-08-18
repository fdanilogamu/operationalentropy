export const ENUMS = {
  diagnosisStatus: [
    ['not_started', 'Not started'], ['readiness_review', 'Readiness review'],
    ['evidence_collection', 'Evidence collection'], ['direct_validation', 'Direct validation'],
    ['synthesis', 'Synthesis'], ['report_drafting', 'Report drafting'],
    ['client_validation', 'Client validation'], ['delivered', 'Delivered'], ['closed', 'Closed']
  ],
  workflowStatus: [
    ['not_started', 'Not started'], ['in_progress', 'In progress'], ['complete', 'Complete'],
    ['complete_with_limitations', 'Complete with limitations'], ['blocked', 'Blocked']
  ],
  requirementStatus: [
    ['received', 'Received'], ['partially_received', 'Partially received'],
    ['confirmed_pending', 'Confirmed but pending'], ['not_received', 'Not received'],
    ['not_available', 'Not available'], ['not_applicable', 'Not applicable']
  ],
  interviewStatus: [
    ['not_scheduled', 'Not scheduled'], ['scheduled', 'Scheduled'], ['in_progress', 'In progress'],
    ['complete', 'Complete'], ['follow_up_required', 'Follow-up required'],
    ['skipped', 'Skipped'], ['cancelled', 'Cancelled']
  ],
  evidenceType: [
    ['observed_fact', 'Observed fact'], ['recorded_fact', 'Recorded fact'], ['estimate', 'Estimate'],
    ['perception', 'Perception'], ['practitioner_inference', 'Practitioner inference']
  ],
  confidence: [['high', 'High'], ['medium', 'Medium'], ['low', 'Low'], ['unavailable', 'Unavailable']],
  metricState: [
    ['not_started', 'Not started'], ['evidence_incomplete', 'Evidence incomplete'],
    ['calculated', 'Calculated'], ['estimated', 'Estimated'], ['confirmed', 'Confirmed'],
    ['overridden', 'Overridden'], ['unavailable', 'Unavailable']
  ],
  toolClassification: [
    ['necessary_distinct', 'Necessary and distinct'], ['necessary_overlapping', 'Necessary but overlapping'],
    ['useful_underutilized', 'Useful but underutilized'], ['specialized_low_frequency', 'Specialized low-frequency utility'],
    ['candidate_consolidation', 'Candidate for consolidation'], ['operational_deadweight', 'Operational deadweight'],
    ['insufficient_evidence', 'Insufficient evidence']
  ],
  founderMemory: [
    ['yes', 'Founder-memory-dependent'], ['no', 'Not founder-memory-dependent'],
    ['insufficient_evidence', 'Insufficient evidence'], ['not_assessed', 'Not assessed']
  ],
  documentStatus: [
    ['current_usable', 'Current and usable'], ['materially_obsolete', 'Materially obsolete'],
    ['insufficient_evidence', 'Insufficient evidence'], ['not_assessed', 'Not assessed']
  ],
  yesNoAssessment: [['yes', 'Yes'], ['no', 'No'], ['not_assessed', 'Not assessed']],
  manualIntervention: [['required', 'Required'], ['not_required', 'Not required'], ['not_assessed', 'Not assessed']],
  integrationOutcome: [
    ['successful', 'Successful'], ['failed', 'Failed'],
    ['insufficient_evidence', 'Insufficient evidence'], ['not_tested', 'Not tested']
  ],
  handoffPresence: [
    ['present', 'Present'], ['missing', 'Missing'], ['not_applicable', 'Not applicable'], ['not_assessed', 'Not assessed']
  ],
  contextLoss: [
    [1, '1 — Context is complete and immediately usable'],
    [2, '2 — Minor gaps rarely impede progress'],
    [3, '3 — Important context sometimes requires reconstruction'],
    [4, '4 — Major gaps frequently delay or distort work'],
    [5, '5 — Handoffs routinely require substantial reconstruction']
  ],
  recommendationLevel: [
    ['immediate_containment', 'Immediate containment'], ['structural_correction', 'Structural correction'],
    ['capability_building', 'Capability building']
  ],
  priority: [['critical', 'Critical'], ['high', 'High'], ['medium', 'Medium'], ['low', 'Low']]
};

export const enumValues = name => ENUMS[name].map(([value]) => value);
export const enumLabel = (name, value) => ENUMS[name].find(([candidate]) => String(candidate) === String(value))?.[1] ?? value ?? '';
export const isEnumValue = (name, value) => enumValues(name).some(candidate => String(candidate) === String(value));

const legacy = {
  diagnosisStatus: {'Not started':'not_started','Readiness review':'readiness_review','Evidence collection':'evidence_collection','Direct validation':'direct_validation','Synthesis':'synthesis','Report drafting':'report_drafting','Client validation':'client_validation','Delivered':'delivered','Closed':'closed'},
  requirementStatus: {'Received':'received','Partially received':'partially_received','Confirmed but pending':'confirmed_pending','Not received':'not_received','Not available':'not_available','Not applicable':'not_applicable'},
  interviewStatus: {'Not scheduled':'not_scheduled','Scheduled':'scheduled','In progress':'in_progress','Complete':'complete','Follow-up required':'follow_up_required','Skipped':'skipped','Cancelled':'cancelled'},
  evidenceType: {'Observed fact':'observed_fact','Recorded fact':'recorded_fact','Estimate':'estimate','Perception':'perception','Practitioner inference':'practitioner_inference'},
  confidence: {'High':'high','Medium':'medium','Low':'low','Unavailable':'unavailable'},
  toolClassification: {'Necessary and distinct':'necessary_distinct','Necessary but overlapping':'necessary_overlapping','Useful but underutilized':'useful_underutilized','Specialized low-frequency utility':'specialized_low_frequency','Candidate for consolidation':'candidate_consolidation','Operational deadweight':'operational_deadweight','Insufficient evidence':'insufficient_evidence'},
  founderMemory: {'Yes':'yes','No':'no','Founder-memory-dependent':'yes','Not founder-memory-dependent':'no','Insufficient evidence':'insufficient_evidence','Not assessed':'not_assessed'},
  documentStatus: {'Yes':'materially_obsolete','No':'current_usable','Current and usable':'current_usable','Materially obsolete':'materially_obsolete','Insufficient evidence':'insufficient_evidence','Not assessed':'not_assessed'},
  integrationOutcome: {'Yes':'successful','No':'failed','Successful':'successful','Failed':'failed','Insufficient evidence':'insufficient_evidence','Not tested':'not_tested'},
  recommendationLevel: {'Immediate containment':'immediate_containment','Structural correction':'structural_correction','Capability building':'capability_building'},
  priority: {'Critical':'critical','High':'high','Medium':'medium','Low':'low'}
};

export function normalizeEnum(name, value) {
  if (value === '' || value == null) return {value: '', changed: false};
  if (isEnumValue(name, value)) return {value, changed: false};
  if (Object.hasOwn(legacy[name] || {}, value)) return {value: legacy[name][value], changed: true};
  return {value, changed: false, unknown: true};
}

export const TOOL_REASON_REQUIRED = new Set(['candidate_consolidation', 'operational_deadweight', 'insufficient_evidence']);
export const REQUIREMENT_LIMITATION_STATUSES = new Set(['partially_received', 'confirmed_pending', 'not_received', 'not_available', 'not_applicable']);
