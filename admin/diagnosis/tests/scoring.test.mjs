import assert from 'node:assert/strict';
import {DIMENSIONS,METRICS,normalizeScore,calculateOEI} from '../scoring.mjs';
import {blankDiagnosis,validateCheckpoint} from '../model.mjs';

const near=(actual,expected)=>assert.ok(Math.abs(actual-expected)<.0001,`${actual} != ${expected}`);
assert.equal(normalizeScore('',10,30,'higher_worse'),null,'blank is missing');
for(const [raw,score] of [[0,2],[10,2],[20,6],[30,10],[40,10]])near(normalizeScore(raw,10,30,'higher_worse'),score);
for(const [raw,score] of [[110,2],[100,2],[50,6],[0,10]])near(normalizeScore(raw,100,0,'lower_worse'),score);
for(const [raw,score] of [[1,2],[2,2],[3,4.6666667],[4,7.3333333],[5,10]])near(normalizeScore(raw,2,5,'higher_worse'),score);
const blank=blankDiagnosis();let result=calculateOEI(blank.metricRecords);assert.equal(result.displayScore,null);assert.equal(result.final,false);
const first=METRICS[0];blank.metricRecords[first.id]={...blank.metricRecords[first.id],calculatedValue:first.healthy,state:'confirmed',confidence:'high',evidenceBasis:'Direct sample',sampleSize:'5'};result=calculateOEI(blank.metricRecords);assert.equal(result.dimensions[first.dimensionId].final,false);assert.equal(result.final,false);assert.equal(result.displayScore,2);
for(const metric of METRICS)blank.metricRecords[metric.id]={...blank.metricRecords[metric.id],calculatedValue:metric.healthy,state:'confirmed',confidence:'high',evidenceBasis:'Direct sample',sampleSize:'5'};result=calculateOEI(blank.metricRecords);assert.equal(result.final,true);near(result.finalScore,2);for(const d of DIMENSIONS)near(result.dimensions[d.id].score,2);
blank.metricRecords[first.id].state='unavailable';blank.metricRecords[first.id].confidence='unavailable';blank.metricRecords[first.id].calculatedValue='';result=calculateOEI(blank.metricRecords);assert.equal(result.final,false);assert.equal(result.metricResults.find(x=>x.id===first.id).score,null);near(result.provisionalScore,2);
const check=validateCheckpoint(blank);assert.equal(check.valid,true);const old=structuredClone(blank);old.scoringSpecVersion='0.0';assert.equal(validateCheckpoint(old).warnings.length,1);
console.log('OEI scoring and checkpoint conformance tests passed.');
