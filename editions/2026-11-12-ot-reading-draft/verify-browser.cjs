'use strict';
// Run from anywhere. Override PLAYWRIGHT_PATH / CHROMIUM_PATH for another host.
const fs = require('node:fs');
const path = require('node:path');
const {pathToFileURL} = require('node:url');
const crypto = require('node:crypto');
const assert = require('node:assert/strict');
const {chromium} = require(process.env.PLAYWRIGHT_PATH || 'C:/Users/penna/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async()=>{
  const browser=await chromium.launch({headless:true,executablePath:process.env.CHROMIUM_PATH || 'C:/Program Files/Google/Chrome/Application/chrome.exe'});
  const checks=[];
  const manifest=JSON.parse(fs.readFileSync(path.join(__dirname,'manifest.json'),'utf8'));
  const page=await browser.newPage({viewport:{width:1440,height:1000}});
  const errors=[];page.on('pageerror',e=>errors.push(String(e)));
  const url=pathToFileURL(path.join(__dirname,'Saints-English-Old-Testament.html')).href;
  await page.goto(url,{waitUntil:'load'});
  assert.equal(await page.locator('.book').count(),43);checks.push('All 43 books available');
  assert.equal(await page.locator('[data-reading-key]').count(),26587);checks.push('26,580 units and seven continuations rendered');
  assert.equal(await page.locator('.candidate').count(),manifest.counts.proposed_changed_units);checks.push(`${manifest.counts.proposed_changed_units} proposals visibly marked`);
  assert.equal(await page.locator('.chapter').count(),1037);checks.push('All 1,037 reading sections rendered');
  await page.screenshot({path:path.join(__dirname,'reader-desktop.png')});
  await page.selectOption('#book-picker','jonah');
  assert.equal(await page.locator('.book:visible').count(),1);
  assert.equal(await page.locator('.book:visible').getAttribute('data-book'),'jonah');checks.push('Book picker shows Jonah only');
  await page.locator('[data-book-link="genesis"]').click();
  assert.equal(await page.locator('.book:visible').getAttribute('data-book'),'genesis');checks.push('Book links update filtered view');
  const proposal=page.locator('#genesis-section-1-v1-25');
  await proposal.locator('summary').click();
  assert.equal(await proposal.locator('details').getAttribute('open'),'');checks.push('Proposal exposes inherited wording and evidence');
  await page.goto(url+'#daniel-section-13');
  assert.equal(await page.locator('.book:visible').getAttribute('data-book'),'daniel');checks.push('Deep link opens Daniel additions');
  await page.emulateMedia({media:'print'});
  assert.equal(await page.locator('.book:visible').count(),43);checks.push('Print includes every book despite screen filter');
  await page.emulateMedia({media:'screen'});
  await page.setViewportSize({width:390,height:844});
  await page.goto(url);
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));checks.push('No horizontal overflow at 390px');
  await page.screenshot({path:path.join(__dirname,'reader-mobile.png')});
  await page.selectOption('#book-picker','jonah');
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));checks.push('Selected-book view fits 390px');
  await page.screenshot({path:path.join(__dirname,'reader-mobile-jonah.png')});
  await page.locator('a[href="#jonah-section-4"]').click();
  const jonahProposal=page.locator('#jonah-section-4-v4-10');
  await jonahProposal.locator('summary').click();
  await jonahProposal.scrollIntoViewIfNeeded();
  assert.equal(await jonahProposal.locator('details').getAttribute('open'),'');
  assert((await jonahProposal.innerText()).includes('You had pity on the gourd'));checks.push('Jonah 4 proposal and inherited comparison are readable on mobile');
  await page.screenshot({path:path.join(__dirname,'reader-mobile-jonah-proposal.png')});
  await page.goto(url+'#genesis-section-4');
  const alignedVerse=page.locator('#genesis-section-4-v4-7');
  await alignedVerse.locator('summary').click();
  assert((await alignedVerse.innerText()).includes('The source words have an explicit AI alignment'));
  assert((await alignedVerse.innerText()).includes('Pronoun antecedents'));
  assert((await alignedVerse.innerText()).includes('Close working draft'));
  await alignedVerse.scrollIntoViewIfNeeded();
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
  checks.push('Genesis 4:7 exposes token status, close alternative and unresolved interpretation on mobile');
  await page.screenshot({path:path.join(__dirname,'reader-mobile-genesis-4-7.png')});
  await page.goto(url+'#exodus-section-2');
  const exodusProposal=page.locator('#exodus-section-2-v2-20');
  await exodusProposal.locator('summary').click();
  assert((await exodusProposal.locator('.reading-text').innerText()).includes('like this'));
  assert(!(await exodusProposal.locator('.baseline').innerText()).includes('like this'));
  assert((await exodusProposal.locator('a[href="https://www.die-bibel.de/en/bible/LXX/EXO.2"]').count())===1);
  await exodusProposal.scrollIntoViewIfNeeded();
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
  checks.push('Exodus 2:20 proposal separates candidate, inherited wording and Greek source');
  await page.screenshot({path:path.join(__dirname,'reader-mobile-exodus-2-20.png')});
  await page.goto(url+'#leviticus-section-3');
  const leviticusProposal=page.locator('#leviticus-section-3-v3-14');
  await leviticusProposal.locator('summary').click();
  assert((await leviticusProposal.locator('.reading-text').innerText()).includes('And upon it'));
  assert((await leviticusProposal.locator('.baseline').innerText()).includes('And from it'));
  assert((await leviticusProposal.innerText()).includes('Referent of upon it'));
  await leviticusProposal.scrollIntoViewIfNeeded();
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
  checks.push('Leviticus flat-schema proposal retains reference, before/after wording and unresolved referent');
  await page.screenshot({path:path.join(__dirname,'reader-mobile-leviticus-3-14.png')});
  for (const [section,anchor,candidate,baseline] of [[5,'v5-7','animal from the flock','sheep'],[11,'v11-27','on its paws','on its hands']]) {
    await page.goto(url+`#leviticus-section-${section}`);
    const proposal=page.locator(`#leviticus-section-${section}-${anchor}`);
    await proposal.locator('summary').click();
    assert((await proposal.locator('.reading-text').innerText()).includes(candidate));
    assert((await proposal.locator('.baseline').innerText()).includes(baseline));
    await proposal.scrollIntoViewIfNeeded();
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
    checks.push(`Leviticus ${anchor.slice(1).replace('-',':')} proposal and baseline visible on mobile`);
    await page.screenshot({path:path.join(__dirname,`reader-mobile-leviticus-${anchor.slice(1)}.png`)});
  }
  for (const [section,anchor,candidate,baseline] of [[2,'v2-17','shall set out in the middle','shall be raised in the middle'],[4,'v4-36','two thousand two hundred fifty','two thousand seven hundred fifty'],[25,'v25-8','kiln','chamber']]) {
    await page.goto(url+`#numbers-section-${section}`);
    const proposal=page.locator(`#numbers-section-${section}-${anchor}`);
    await proposal.locator('summary').click();
    assert((await proposal.locator('.reading-text').innerText()).includes(candidate));
    assert((await proposal.locator('.baseline').innerText()).includes(baseline));
    await proposal.scrollIntoViewIfNeeded();
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
    checks.push(`Numbers ${anchor.slice(1).replace('-',':')} proposal and baseline visible on mobile`);
    await page.screenshot({path:path.join(__dirname,`reader-mobile-numbers-${anchor.slice(1)}.png`)});
  }
  await page.goto(url+'#deuteronomy-section-18');
  const deuProposal=page.locator('#deuteronomy-section-18-v18-20');
  await deuProposal.locator('summary').click();
  assert((await deuProposal.locator('.reading-text').innerText()).includes('which I did not command him to speak'));
  assert((await deuProposal.locator('.baseline').innerText()).includes('which I commanded him not to speak'));
  await deuProposal.scrollIntoViewIfNeeded();
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
  checks.push('Deuteronomy 18:20 negation correction and baseline are distinct on mobile');
  await page.screenshot({path:path.join(__dirname,'reader-mobile-deuteronomy-18-20.png')});
  await page.goto(url+'#deuteronomy-section-32');
  const song=page.locator('#deuteronomy-section-32-v32-43');
  assert.equal((await song.locator('.reading-text').innerText()).split('\n').length,8);
  await song.locator('summary').click();
  assert((await song.innerText()).includes('Poetic line breaks proposed by AI'));
  assert((await song.innerText()).includes('sons of God'));
  assert((await song.innerText()).includes('angels of God'));
  await song.scrollIntoViewIfNeeded();
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
  checks.push('Deuteronomy 32:43 retains all eight poetic clauses and identifies proposed lineation');
  await song.screenshot({path:path.join(__dirname,'reader-mobile-deuteronomy-32-43.png')});
  await page.goto(url+'#deuteronomy-section-33');
  const ambiguous=page.locator('#deuteronomy-section-33-v33-3');
  await ambiguous.locator('summary').click();
  assert((await ambiguous.innerText()).includes('Moses as addressee'));
  assert((await ambiguous.innerText()).includes('Thy hands'));
  await ambiguous.scrollIntoViewIfNeeded();
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
  checks.push('Deuteronomy 33:3 exposes the unresolved divine-address interpretation');
  await ambiguous.screenshot({path:path.join(__dirname,'reader-mobile-deuteronomy-33-3.png')});
  await page.goto(url+'#joshua-section-15');
  const bethlehem=page.locator('#joshua-section-15-v15-59a');
  assert((await bethlehem.locator('.reading-text').innerText()).includes('Bethlehem'));
  assert((await bethlehem.locator('.reading-text').innerText()).includes('eleven cities'));
  await bethlehem.locator('summary').click();
  await bethlehem.scrollIntoViewIfNeeded();
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
  checks.push('Joshua 15:59a lettered Bethlehem-area list and comparison remain accessible on mobile');
  await page.screenshot({path:path.join(__dirname,'reader-mobile-joshua-15-59a.png')});
  await page.goto(url+'#joshua-section-22');
  const purpose=page.locator('#joshua-section-22-v22-24');
  await purpose.locator('summary').click();
  assert((await purpose.locator('.reading-text').innerText()).includes('so that your children may not say'));
  assert((await purpose.locator('.baseline').innerText()).includes('Tomorrow your children might say'));
  assert((await purpose.innerText()).includes('supplied English grammatical support'));
  await purpose.scrollIntoViewIfNeeded();
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
  checks.push('Joshua 22:24 negative-purpose proposal, baseline and supplied-grammar explanation are distinct');
  await page.screenshot({path:path.join(__dirname,'reader-mobile-joshua-22-24.png')});
  const salamin=page.locator('#joshua-section-22-v22-29');
  await salamin.locator('summary').click();
  assert((await salamin.locator('.reading-text').innerText()).includes('salamin sacrifices'));
  assert((await salamin.locator('.reading-text').innerText()).includes('sacrifice of deliverance'));
  assert((await salamin.innerText()).includes('remains unresolved'));
  await salamin.scrollIntoViewIfNeeded();
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
  checks.push('Joshua 22:29 keeps salamin separate from the revised ritual label and exposes its uncertainty');
  await page.screenshot({path:path.join(__dirname,'reader-mobile-joshua-22-29.png')});
  await page.goto(url+'#joshua-section-24');
  const ending=page.locator('#joshua-section-24-v24-33b');
  assert((await ending.locator('.reading-text').innerText()).includes('Eglom'));
  assert((await ending.locator('.reading-text').innerText()).includes('eighteen years'));
  await ending.locator('summary').click();
  await ending.scrollIntoViewIfNeeded();
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
  checks.push('Joshua longer ending remains accessible with its full final lettered unit');
  await page.screenshot({path:path.join(__dirname,'reader-mobile-joshua-24-33b.png')});
  assert.equal(await page.locator('[data-book="joshua"] [data-reading-key]').count(),659);
  checks.push('All 659 Joshua stored units remain rendered with stable identities');
  await page.goto(url+'#judges-section-5');
  const deborah=page.locator('#judges-section-5-v5-4');
  assert.equal((await deborah.locator('.reading-text').innerText()).split('\n').length,5);
  await deborah.locator('summary').click();
  assert((await deborah.innerText()).includes('Poetic line breaks proposed by AI'));
  assert((await deborah.locator('.reading-text').innerText()).includes('Thou didst'));
  await deborah.scrollIntoViewIfNeeded();
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
  checks.push('Judges 5:4 preserves five poetic lines and divine address with explicit AI lineation status');
  await deborah.screenshot({path:path.join(__dirname,'reader-mobile-judges-5-4.png')});
  for (const [section,anchor,required] of [[11,'v11-31',['whoever','and I will offer','whole burnt offering','No or, alternative dedication']], [21,'v21-22',['you committed an offence','not negated','Pronoun shifts']]]) {
    await page.goto(url+`#judges-section-${section}`);
    const unit=page.locator(`#judges-section-${section}-${anchor}`);
    await unit.locator('summary').click();
    for (const phrase of required) assert((await unit.innerText()).includes(phrase),phrase);
    await unit.scrollIntoViewIfNeeded();
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
    checks.push(`Judges ${anchor.slice(1).replace('-',':')} selected difficult reading and interpretation limits remain accessible`);
    await unit.screenshot({path:path.join(__dirname,`reader-mobile-judges-${anchor.slice(1)}.png`)});
  }
  for (const [section,anchor,candidate,baseline] of [[12,'v12-5','And they said, “We are not.”','And if they said'],[19,'v19-28','but she had died','for she had died']]) {
    await page.goto(url+`#judges-section-${section}`);
    const unit=page.locator(`#judges-section-${section}-${anchor}`);
    await unit.locator('summary').click();
    assert((await unit.locator('.reading-text').innerText()).includes(candidate));
    assert((await unit.locator('.baseline').innerText()).includes(baseline));
    await unit.scrollIntoViewIfNeeded();
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
    checks.push(`Judges ${anchor.slice(1).replace('-',':')} proposal is distinguished from its inherited text`);
    await unit.screenshot({path:path.join(__dirname,`reader-mobile-judges-${anchor.slice(1)}.png`)});
  }
  assert.equal(await page.locator('[data-book="judges"] [data-reading-key]').count(),618);
  checks.push('All 618 Judges stored units remain rendered with stable identities');
  await page.goto(url+'#ruth-section-1');
  const pledge=page.locator('#ruth-section-1-v1-17');
  await pledge.locator('summary').click();
  assert.equal((await pledge.locator('.reading-text').innerText()).split('\n').length,5);
  assert((await pledge.locator('.reading-text').innerText()).includes('death shall part me and you'));
  assert((await pledge.innerText()).includes('Poetic line breaks proposed by AI'));
  await pledge.scrollIntoViewIfNeeded();
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
  checks.push('Ruth 1:17 retains ordinary human address, affirmative death clause and five proposed poetic lines');
  await pledge.screenshot({path:path.join(__dirname,'reader-mobile-ruth-1-17.png')});
  await page.goto(url+'#ruth-section-2');
  const blessing=page.locator('#ruth-section-2-v2-12');
  await blessing.locator('summary').click();
  assert((await blessing.locator('.reading-text').innerText()).endsWith('trust.”'));
  assert((await blessing.locator('.baseline').innerText()).endsWith('trust.'));
  assert((await page.locator('#ruth-section-2-v2-13 .reading-text').innerText()).startsWith('She said, “'));
  await blessing.scrollIntoViewIfNeeded();
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
  checks.push('Ruth 2:12 closes Boaz speech before Ruth speaks and retains the exact unclosed baseline');
  await blessing.screenshot({path:path.join(__dirname,'reader-mobile-ruth-2-12.png')});
  await page.goto(url+'#ruth-section-3');
  const entrant=page.locator('#ruth-section-3-v3-15');
  await entrant.locator('summary').click();
  assert((await entrant.innerText()).includes('final entrant is especially unresolved'));
  assert((await entrant.locator('.reading-text').innerText()).includes('six measures of barley'));
  await entrant.scrollIntoViewIfNeeded();
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
  checks.push('Ruth 3:15 preserves unspecified measures and exposes the unexpressed-subject question');
  await entrant.screenshot({path:path.join(__dirname,'reader-mobile-ruth-3-15.png')});
  assert.equal(await page.locator('[data-book="ruth"] [data-reading-key]').count(),85);
  assert((await page.locator('#ruth-section-4-v4-4 .reading-text').innerText()).includes('For there is no one'));
  checks.push('All 85 Ruth units remain rendered and the 4:4 explanatory link is present');
  assert.equal(await page.locator('[data-book="1-samuel"] [data-reading-key]').count(),773);
  assert.equal(await page.locator('[id="1-samuel-section-13-v13-1"]').count(),0);
  assert.equal(await page.locator('[id="1-samuel-section-23-v23-12"]').count(),0);
  assert.equal(await page.locator('[id="1-samuel-section-17"] [data-reading-key]').count(),32);
  assert.equal(await page.locator('[id="1-samuel-section-18"] [data-reading-key]').count(),19);
  checks.push('All 773 1 Samuel units preserve selected omissions and shorter chapters 17–18');
  for (const [section,anchor,phrases] of [[2,'v2-10',['our kings','wisdom','Poetic line breaks proposed by AI']],[2,'v2-33',['spare a man of yours at My altar','not destroy every man','indefinite’s exact scope']],[20,'v20-12',['shall I not send','conditional negative']],[21,'v21-6',['because of my equipment','through my equipment','dia takes the accusative']],[30,'v30-28a',['Gath','Kinan','Saphek','Thimath']]]) {
    await page.goto(url+`#1-samuel-section-${section}`);
    const unit=page.locator(`[id="1-samuel-section-${section}-${anchor}"]`);
    await unit.locator('summary').click();
    for (const phrase of phrases) assert((await unit.innerText()).includes(phrase),phrase);
    if(anchor==='v2-10') assert.equal((await unit.locator('.reading-text').innerText()).split('\n').length,12);
    await unit.scrollIntoViewIfNeeded();
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
    checks.push(`1 Samuel ${anchor.slice(1).replace('-',':')} selected wording and comparison remain accessible on mobile`);
    await unit.screenshot({path:path.join(__dirname,`reader-mobile-1-samuel-${anchor.slice(1)}.png`)});
  }
  assert.equal(await page.locator('[data-book="2-samuel"] [data-reading-key]').count(),696);
  assert.equal(await page.locator('[id="2-samuel-section-5"] [data-reading-key]').count(),26);
  assert.equal(await page.locator('[id="2-samuel-section-18-v18-33"]').count(),0);
  checks.push('All 696 2 Samuel units preserve 5:16a and the lament boundary at 19:1');
  for (const [section,anchor,phrases] of [[5,'v5-16a',['Samae','Eliphalath','All thirteen names']],[16,'v16-18',['I will follow the one','From now on','supplies a finite English predicate']],[19,'v19-1',['my son, my son','Five authored lines']],[19,'v19-23',['I do not know whether I reign','not converted']],[22,'v22-17',['He sent from on high','He reached from on high','object of sent is unexpressed']],[23,'v23-8',['eight hundred wounded men','eight hundred who were slain']],[24,'v24-25',['Solomon enlarged the altar','initial smallness']]]) {
    await page.goto(url+`#2-samuel-section-${section}`);
    const unit=page.locator(`[id="2-samuel-section-${section}-${anchor}"]`);
    await unit.locator('summary').click();
    for (const phrase of phrases) assert((await unit.innerText()).includes(phrase),phrase);
    if(anchor==='v19-1') assert.equal((await unit.locator('.reading-text').innerText()).split('\n').length,5);
    if(anchor==='v22-17') assert.equal((await unit.locator('.reading-text').innerText()).split('\n').length,2);
    await unit.scrollIntoViewIfNeeded();
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
    checks.push(`2 Samuel ${anchor.slice(1).replace('-',':')} selected wording and evidence remain accessible on mobile`);
    await unit.screenshot({path:path.join(__dirname,`reader-mobile-2-samuel-${anchor.slice(1)}.png`)});
  }
  assert.equal(await page.locator('[data-book="1-kings"] [data-reading-key]').count(),823);
  assert.equal(await page.locator('[data-book="1-kings"] .verse').count(),822);
  assert.equal(await page.locator('[id="1-kings-section-2"] .verse').count(),71);
  assert.equal(await page.locator('[id="1-kings-section-12"] .verse').count(),54);
  checks.push('All 822 1 Kings units and its attached continuation retain stable identities and expanded chapters');
  for (const id of ['1-kings-section-3-v3-1','1-kings-section-6-v6-18','1-kings-section-14-v14-1','1-kings-section-22-v22-47']) {
    assert.equal(await page.locator(`[id="${id}"]`).count(),0);
  }
  assert.equal(await page.locator('[id="1-kings-section-11-v11-5-8"]').count(),1);
  checks.push('1 Kings selected gaps and the combined 11:5–8 unit remain intact');
  for (const [section,anchor,phrases] of [[3,'v3-27',['Give it to her, and you must not put him to death.','inner quotation']],[8,'v8-53a',['Book of Song','dwelling in newness','Speaker boundaries']],[10,'v10-7',['what they reported to me is not half of it','not half as they reported to me']],[12,'v12-24b',['three hundred','Sarira']],[16,'v16-9',['Elah was in Tirzah','He was in Tirzah']],[17,'v17-23',['Look, your son lives','Behold, your son lives']],[22,'v22-34',['good aim','lung and the breastplate','anatomy']]]) {
    await page.goto(url+`#1-kings-section-${section}`);
    const unit=page.locator(`[id="1-kings-section-${section}-${anchor}"]`);
    await unit.locator('summary').click();
    for (const phrase of phrases) assert((await unit.innerText()).includes(phrase),phrase);
    if(anchor==='v8-53a') {
      assert.equal(await unit.locator('.reading-text').count(),2);
      assert.equal((await unit.locator('.reading-text').nth(0).innerText()).split('\n').length,2);
      assert.equal((await unit.locator('.reading-text').nth(1).innerText()).split('\n').length,4);
      assert((await unit.innerText()).includes('Poetic line breaks proposed by AI'));
    }
    await unit.scrollIntoViewIfNeeded();
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
    checks.push(`1 Kings ${anchor.slice(1).replace('-',':')} selected wording and evidence remain accessible on mobile`);
    await unit.screenshot({path:path.join(__dirname,`reader-mobile-1-kings-${anchor.slice(1)}.png`)});
  }
  assert.equal(await page.locator('[data-book="2-kings"] [data-reading-key]').count(),723);
  assert.equal(await page.locator('[data-book="2-kings"] .verse').count(),723);
  assert.equal(await page.locator('[id="2-kings-section-1"] .verse').count(),22);
  for (const suffix of ['a','b','c','d']) assert.equal(await page.locator(`[id="2-kings-section-1-v1-18${suffix}"]`).count(),1);
  assert((await page.locator('[id="2-kings-section-25-v25-30"] .reading-text').innerText()).includes('all the days of his life'));
  checks.push('All 723 2 Kings units preserve the four 1:18 lettered units and the final daily provision');
  assert((await page.locator('[id="2-kings-section-25-v25-9"] .reading-text').innerText()).endsWith('by'));
  assert.equal(await page.locator('[id="2-kings-section-25-v25-10"] .reading-text').innerText(),'the chief cook.');
  checks.push('The selected 2 Kings 25:9–10 sentence split remains intact without an imported wall-demolition clause');
  for (const [section,anchor,phrases] of [[1,'v1-9',['behold, Elijah was sitting','comma between was and sitting']],[2,'v2-14',['Appho','first strike']],[6,'v6-27',['May the Lord not save you','negative wish']],[9,'v9-6',['The prophet poured','He poured','subject is inferred']],[13,'v13-11',['any sin','every sin']],[17,'v17-34',['the sons of Jacob','They fear','no negations']],[19,'v19-23',['you reproached the Lord and said','you did reproach','melon']],[22,'v22-19',['you felt shame','you did feel shame']],[25,'v25-10',['the chief cook.','grammatical completion']]]) {
    await page.goto(url+`#2-kings-section-${section}`);
    const unit=page.locator(`[id="2-kings-section-${section}-${anchor}"]`);
    await unit.locator('summary').click();
    for (const phrase of phrases) assert((await unit.innerText()).includes(phrase),phrase);
    if(anchor==='v19-23') assert.equal((await unit.locator('.reading-text').innerText()).split('\n').length,4);
    await unit.scrollIntoViewIfNeeded();
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
    checks.push(`2 Kings ${anchor.slice(1).replace('-',':')} selected wording and evidence remain accessible on mobile`);
    await unit.screenshot({path:path.join(__dirname,`reader-mobile-2-kings-${anchor.slice(1)}.png`)});
  }
  assert.equal(await page.locator('[data-book="1-chronicles"] .verse').count(),930);
  assert.equal(await page.locator('[id="1-chronicles-section-1"] .verse').count(),42);
  assert.equal(await page.locator('[id="1-chronicles-section-5"] .verse').count(),41);
  assert.equal(await page.locator('[id="1-chronicles-section-6"] .verse').count(),66);
  for (const verse of [11,12,13,14,15,16,18,19,20,21,22,23]) assert.equal(await page.locator(`[id="1-chronicles-section-1-v1-${verse}"]`).count(),0);
  assert.equal(await page.locator('[id="1-chronicles-section-16-v16-24"]').count(),0);
  assert((await page.locator('[id="1-chronicles-section-29-v29-30"] .reading-text').innerText()).endsWith('all the kingdoms of the earth.'));
  checks.push('All 930 1 Chronicles units preserve selected chapter boundaries, Genesis-list and psalm gaps, and the final record notice');
  for (const [section,anchor,phrases,lines] of [[1,'v1-29',['generations of Ishmael, the firstborn','Ishmael’s firstborn'],0],[5,'v5-21',['one hundred thousand men','human lives'],0],[9,'v9-11',['Azaria, leader of the house of God','son of Achitob'],0],[10,'v10-1',['The Israelites fled','They fled'],0],[10,'v10-14',['and the Lord killed him','and He killed him'],0],[12,'v12-19',['A spirit clothed Amasai','Poetic line breaks proposed by AI'],7],[16,'v16-35',['Thy holy name','Poetic line breaks proposed by AI'],4],[19,'v19-14',['and the Syrians fled','and they fled'],0],[27,'v27-5',['Banaias, priest and ruler, son of Jodae','nominative titles'],0]]) {
    await page.goto(url+`#1-chronicles-section-${section}`);
    const unit=page.locator(`[id="1-chronicles-section-${section}-${anchor}"]`);
    await unit.locator('summary').click();
    for (const phrase of phrases) assert((await unit.innerText()).includes(phrase),phrase);
    if(lines) assert.equal((await unit.locator('.reading-text').innerText()).split('\n').length,lines);
    await unit.scrollIntoViewIfNeeded();
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
    checks.push(`1 Chronicles ${anchor.slice(1).replace('-',':')} selected wording, provisional evidence and display remain accessible on mobile`);
    await unit.screenshot({path:path.join(__dirname,`reader-mobile-1-chronicles-${anchor.slice(1)}.png`)});
  }
  assert.equal(await page.locator('[data-book="2-chronicles"] .verse').count(),833);
  assert.equal(await page.locator('[id="2-chronicles-section-27"] .verse').count(),8);
  assert.equal(await page.locator('[id="2-chronicles-section-27-v27-8"]').count(),0);
  for (const [section,anchors] of [[35,['19a','19b','19c','19d']],[36,['2a','2b','2c','4a','5a','5b','5c','5d']]]) {
    for (const anchor of anchors) assert.equal(await page.locator(`[id="2-chronicles-section-${section}-v${section}-${anchor}"]`).count(),1);
  }
  assert((await page.locator('[id="2-chronicles-section-36-v36-23"] .reading-text').innerText()).endsWith('and let him go up.”'));
  checks.push('All 833 2 Chronicles units preserve the gap at 27:8, twelve lettered additions and the final ascent command');
  // The scoped package records provide exact before/after text independently of HTML rendering.
  let twoChroniclesCompared=0;
  for (const folder of fs.readdirSync(path.join(__dirname,'../../reviews')).filter(name=>/^2026-11-13-OT-\d+-2-chronicles-/.test(name))) {
    const records=JSON.parse(fs.readFileSync(path.join(__dirname,'../../reviews',folder,'focused-reviews.json'),'utf8')).records;
    for (const record of records.filter(record=>record.decision==='propose_revision')) {
      const unit=page.locator(`[id="2-chronicles-section-${record.reading_section_id}-${record.verse_anchor}"]`);
      assert.equal((await unit.locator('.reading-text').innerText()).replace(/\s+/g,' ').trim(),record.candidate_text.replace(/\s+/g,' ').trim());
      assert((await unit.textContent()).includes(record.baseline_text));
      twoChroniclesCompared++;
    }
  }
  assert.equal(twoChroniclesCompared,11);
  checks.push('All eleven 2 Chronicles proposals render exact candidate wording and preserve their inherited comparison');
  for (const [section,anchor,phrases,lines] of [[4,'v4-13',['on one network','on each network','distributive'],0],[6,'v6-27',['they will walk','they should walk'],0],[6,'v6-41',['Thy sons','Poetic line breaks proposed by AI'],4],[10,'v10-11',['Now my father','and-now'],0],[14,'v14-4',['he was at peace','he made peace'],0],[19,'v19-10',['Each of you shall','distributive attachment'],0],[20,'v20-21',['Give thanks to the Lord','Poetic line breaks proposed by AI'],3],[25,'v25-15',['that people’s gods, who did not rescue','could not rescue'],0],[25,'v25-19',['You said','You say'],0],[34,'v34-22',['herself keeper of the robes','feminine keeper participle'],0],[34,'v34-24',['Behold, I am bringing','expressly'],0],[35,'v35-25',['male and female rulers','and behold, it is written'],0],[36,'v36-5d',['Jehoiakim shed','did not wish to destroy'],0]]) {
    await page.goto(url+`#2-chronicles-section-${section}`);
    const unit=page.locator(`[id="2-chronicles-section-${section}-${anchor}"]`);
    await unit.locator('summary').click();
    for (const phrase of phrases) assert((await unit.innerText()).includes(phrase),phrase);
    if(lines) assert.equal((await unit.locator('.reading-text').innerText()).split('\n').length,lines);
    await unit.scrollIntoViewIfNeeded();
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
    checks.push(`2 Chronicles ${anchor.slice(1).replace('-',':')} selected wording, provisional evidence and display remain accessible on mobile`);
    await unit.screenshot({path:path.join(__dirname,`reader-mobile-2-chronicles-${anchor.slice(1)}.png`)});
  }
  assert.equal(await page.locator('[data-book="1-maccabees"] .verse').count(),924);
  assert.equal(await page.locator('[id="1-maccabees-section-1"] .verse').count(),64);
  assert.equal(await page.locator('[id="1-maccabees-section-16"] .verse').count(),24);
  assert((await page.locator('[id="1-maccabees-section-16-v16-24"] .reading-text').innerText()).startsWith('behold, these are written'));
  checks.push('All 924 1 Maccabees units preserve their chapter boundaries and final record formula');
  let oneMaccabeesCompared=0;
  for (const folder of fs.readdirSync(path.join(__dirname,'../../reviews')).filter(name=>/^2026-11-13-OT-\d+-1-maccabees-/.test(name))) {
    const records=JSON.parse(fs.readFileSync(path.join(__dirname,'../../reviews',folder,'focused-reviews.json'),'utf8')).records;
    for (const record of records.filter(record=>record.decision==='propose_revision')) {
      const unit=page.locator(`[id="1-maccabees-section-${record.reading_section_id}-${record.verse_anchor}"]`);
      assert.equal((await unit.locator('.reading-text').innerText()).replace(/\s+/g,' ').trim(),record.candidate_text.replace(/\s+/g,' ').trim());
      assert((await unit.textContent()).includes(record.baseline_text));
      oneMaccabeesCompared++;
    }
  }
  assert.equal(oneMaccabeesCompared,20);
  checks.push('All twenty 1 Maccabees proposals render exact candidate wording and preserve inherited text');
  for (const [section,anchor,phrases,lines] of [[1,'v1-15',['were yoked','were sold'],0],[2,'v2-61',['will not grow weak','will not fail'],2],[3,'v3-4',['roaring for prey','roaring over prey'],2],[3,'v3-48',['idol likenesses','interpretive'],0],[4,'v4-24',['For it is good','neuter formula'],3],[5,'v5-58',['He gave orders','They gave orders'],0],[7,'v7-17',['Thy holy ones','Psalm source'],2],[8,'v8-9',['They also reported','They also heard'],0],[8,'v8-28',['those acting as allies','enemy possessive'],0],[9,'v9-54',['and began the demolition','began tearing down'],0],[10,'v10-47',['fought alongside him continually','all his days'],0],[11,'v11-66',['his right hand in pledge','to receive a pledge'],0],[12,'v12-43',['obey Jonathan as they obeyed him','obeyed himself'],0],[13,'v13-28',['seven pyramids','six named relatives'],0],[14,'v14-7',['many captives','many who had been captive'],4],[14,'v14-41',['for ever, until a faithful prophet','prophetic review'],0],[16,'v16-5',['Behold! A large force','restoring Behold'],0]]) {
    await page.goto(url+`#1-maccabees-section-${section}`);
    const unit=page.locator(`[id="1-maccabees-section-${section}-${anchor}"]`);
    await unit.locator('summary').click();
    for (const phrase of phrases) assert((await unit.innerText()).includes(phrase),phrase);
    if(lines) assert.equal((await unit.locator('.reading-text').innerText()).split('\n').length,lines);
    await unit.scrollIntoViewIfNeeded();
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
    checks.push(`1 Maccabees ${anchor.slice(1).replace('-',':')} selected wording, evidence and display remain accessible on mobile`);
    await unit.screenshot({path:path.join(__dirname,`reader-mobile-1-maccabees-${anchor.slice(1)}.png`)});
  }
  await page.locator('#book-picker').focus();
  assert.equal(await page.evaluate(()=>document.activeElement.id),'book-picker');checks.push('Book control is keyboard focusable');
  assert.deepEqual(errors,[]);checks.push('No JavaScript page errors');
  await browser.close();
  fs.writeFileSync(path.join(__dirname,'browser-validation.json'),JSON.stringify({status:'passed',date:manifest.updated,reader_sha256:crypto.createHash('sha256').update(fs.readFileSync(path.join(__dirname,'Saints-English-Old-Testament.html'))).digest('hex'),environment:'Headless Chrome on Windows; local file, 1440×1000 and 390×844',checks,limits:'Automated functional checks and screenshots, not human reading aloud or an accessibility conformance audit.'},null,2)+'\n');
  console.log(JSON.stringify({status:'passed',checks:checks.length},null,2));
})().catch(e=>{console.error(e);process.exitCode=1;});
