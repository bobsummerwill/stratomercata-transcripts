
**SPEAKER_01:**
[1.8s] Okay, welcome everyone.
[3.4s] We have a very special and very timely topic today, privacy on-chain and the rise of Zcash.
[14.6s] And we sort of have a special guest today.
[16.5s] So I'm Victor Wong.
[17.9s] I am founder and chief product officer at BlockApps.
[22.5s] I'll get to our normal guests, but today we have Jim.
[26.5s] Do you want to give us a quick intro?

**SPEAKER_02:**
[29.4s] Yeah, I'm also, I've known Victor and Kieran for years.
[33.1s] I'm one of the founders of BlockApps and CTO.

**SPEAKER_01:**
[37.7s] And you're here in particularly because I would call you a Zcash expert, having written your own Zcash client.

**SPEAKER_02:**
[48.1s] Well, I think I'm more aspirational at this point in time.
[52.9s] I mean, the way I learn about things is I try to...

**SPEAKER_03:**
[56.9s] How many more expert people do you think there are on, say, Zcash in particular on the planet?

**SPEAKER_02:**
[65.3s] No, the problem that I have is that I was sort of halfway in the learning process last year.
[72.2s] So the way I learn about things is I try to like write a client for it.
[75.9s] So I was doing that, but then we got pulled in different directions.
[79.7s] I got to the point where I had sort of replicated the actual client that could connect.
[84.7s] It would bring the data in.
[86.9s] It would bring the proofs in.
[88.3s] But just about when I was getting to the good part, that's when we moved on to other things.

**SPEAKER_03:**
[94.3s] Well, we're going to put the number.
[96.9s] answer my own question right between like 10 and 100. maybe i would say there there's definitely less than 20 people who have written their own zcash clients probably well yeah there's probably some core contributors i imagine there's more than a handful into zcash but you know when jim says non-expert he you know it's like there are let's say yes
[122.1s] I'll expand the range.
[123.1s] Five to 100 people who understand Zcash better on the planet.
[127.5s] Big, big, big range there.
[129.2s] But we're talking about pretty small numbers in absolute terms.
[133.2s] Yes, exactly.

**SPEAKER_01:**
[134.6s] I would say if Jim's not an expert, I don't know what even expert means.
[139.0s] Anyways, Karen, do you want to give a quick intro of yourself?

**SPEAKER_03:**
[143.4s] Certainly.
[143.8s] um i'm our ceo been on these before by the way vick you're letting jim off the hook calling him a special guest he has to do this all the time now with our you know continued in the public so special in the future special today today is special but it's the first of many let's just say that i was looking through the the the prior videos jim has never appeared on one of our own spaces

**SPEAKER_00:**
[174.6s] He's only been on early days of Ethereum.

**SPEAKER_03:**
[177.4s] Okay.

**SPEAKER_01:**
[178.7s] There you go.
[181.0s] But it won't be special soon.
[182.8s] Bob, by the way, since you've spoken up, can you give a quick intro to yourself?

**SPEAKER_00:**
[187.2s] So hi, I'm Bob.
[188.8s] I'm head of ecosystem.
[190.3s] And yeah, been doing a lot of spaces.

**SPEAKER_01:**
[196.2s] Yeah.
[196.7s] So I think, you know, to level set, because I think there's a lot of...
[202.4s] misunderstanding about what privacy is.
[204.7s] How would you define blockchain privacy and why do you think it's important?

**SPEAKER_00:**
[212.0s] Who's that question for?

**SPEAKER_01:**
[213.9s] Could be for anyone, whoever wants to go.
[215.7s] Karen, you want to kick us off?

**SPEAKER_03:**
[218.6s] So, and for the, I assume that the viewer is pretty deep in the space, but I'll bring it down to a fairly low technical level.
[229.2s] So blockchains are great.
[231.6s] They let you move digitally scarce value from party to party.
[237.2s] And the...
[240.0s] way that this is typically done is that you've got a big address which is almost but not quite a public key and you sort of sign a message that says i kieran but it's not kieran because it's this address send you know three bitcoin uh to bob and it doesn't say bob it's another address you don't quite know who either of those parties are however you've got the address forever
[264.9s] And often it is the case that you can piece together what happens based on that address.
[271.5s] So say you're on a centralized exchange which has KYC.
[276.0s] It knows how to associate you to maybe a withdrawal address.
[282.1s] It may not know down the line.
[284.9s] But if you start to get a bunch of data points, you can kind of piece together who sent what to whom.
[292.1s] And you're actually in an extremely transparent scenario where everyone's financial transactions are visible to everyone.
[300.5s] And it's not while it's a cryptographic technology, it's not necessarily a private technology.
[305.8s] and this has been a problem both in the consumer setting just for you know people don't like this satoshi makes a comment i believe in the white paper saying that
[318.5s] know obviously to prevent the double spend problem which basically just is just that um to ensure that bitcoin can't be created or destroyed except by the agreed mechanism um obviously you need to know the whole history and so he sees the problem as intrinsic but some technologies come out later that maybe calls that into question that we'll talk about
[344.3s] It's also an enterprise problem.
[345.8s] So we can talk separately about our experience there.
[349.7s] Sort of what the enterprises want is kind of the same as what the public blockchain people want, except with selective visibility.
[359.6s] So they want to say you're doing like an on-chain stock trade, which is actually now starting to happen.
[366.1s] You sort of want to know the other party has the stock.
[369.1s] You don't necessarily want to know who the other party is.
[374.8s] But you want to know that they acquired that stock legitimately.
[378.7s] And then when you get it, you want to be able to pass it on legitimately in the same way.
[382.6s] And then there's sometimes this extra requirement that like the regulator can see everything, you know.
[387.6s] So you want sort of like a unlinkability of balance to person or company, but also this mass preservation property that I was talking about can't create or destroy assets.
[398.4s] They have to be acquired legitimately.
[402.3s] and so on.
[403.5s] So it's a perennial problem and closer to solved, you know, but we can go into that shortly.

**SPEAKER_01:**
[410.3s] Yeah.
[410.5s] Bob, did you want to add anything to that?

**SPEAKER_00:**
[412.9s] Yeah.
[413.1s] Yes.
[413.3s] I mean, going back to those Bitcoin, you know, beginnings in the Bitcoin white paper, you know, it just talks about severing identity from transactions.
[425.9s] But really, that's just pseudonymous, not anonymous.
[433.0s] And I think a lot of people didn't understand that differentiation back in those early days.
[438.6s] And it's like, oh, Bitcoin's private, untrackable.
[442.4s] you know, digital money.
[446.8s] But, you know, very rapidly you have blockchain analytics coming in, you know, looking for correlations and patterns.
[453.6s] And it's like, yeah, that's, you're not getting a lot of security.
[458.8s] You know, even if you're not reusing addresses, just sort of normal things that people would do, there's lots of correlations and, you know, you can get unmasked that way.
[468.9s] But yeah, Satoshi did talk a bit about zero knowledge.
[474.4s] I can't remember who raised it.
[475.9s] Somebody raised it early and he was like, yeah, that would be interesting if we could do that.
[483.1s] But it was just like a lot of that cryptography just hadn't happened.
[490.7s] So Zcash started in 2016, and it was only around that kind of time or a little before that you started having these papers on SNARK constructions and going through all these different kind of rounds.
[507.4s] So, yeah, I mean, what that's meant is Bitcoin and then Ethereum following that same path.
[514.2s] You know, they are an immutable public ledger forever.
[518.9s] Ethereum even worse because it's an account model.
[522.3s] So you are reusing the addresses all the time, right?
[525.8s] And if your address is unmasked, you are forever doxxed.
[530.5s] That's happened to at least one of the Ethereum founders who moved hundreds of millions of dollars out of a known address of his, which probably not desired.

**SPEAKER_01:**
[545.4s] And I, you know, you guys have been talking about Satoshi, but Jim, I remember, I think it's like earlier at like 2014, Vitalik was talking like, he was like, ZK Snarks will fix all of this at some point in time.
[558.6s] Do you remember that at all?

**SPEAKER_02:**
[560.3s] Well, I mean, like, I think we went through a learning process about privacy and that's sort of like, we're understating this right now.
[569.0s] Maybe it's because we put a lot of time and effort into some privacy solutions that, you
[574.7s] technically worked, but were a business failure, I think is fair to say.
[579.9s] And so, you know, the audience can learn from our like sort of failed mistakes in the past right now.
[586.6s] But we sort of built, so we had heard years ago about CK, but we sort of just, I don't know, at the time looked into it and said like, oh, this looks like overly complicated.
[598.8s] You can get privacy through these other means.
[601.8s] And we ended up building a system that,
[604.3s] that allowed for sort of like quick spin-up of private chains that everything was sort of like in an encrypted tunnel and you could have like these chains completely secure and nobody else would see what was happening there.
[622.3s] But long story short, you know, slow learning process.
[626.8s] We found out that customers want everything and
[634.3s] to the point that it made it worthless.
[636.1s] Like we would go into enterprise, we would say like, oh, you can set up these private channels with others.
[642.2s] And they loved that because they could sort of control that and they could control who goes in there.
[646.2s] But then once everything was going through these private channels, then they wanted to be able to like transfer from private chain to private chain.
[654.2s] And that's where everything started to fall apart.
[656.3s] And getting things back onto the main chain became sort of this extra complicated system.
[664.1s] And at the same time, customers wanted to have like a full flexibility in having like extensions to solidity where you could just like name a chain and send some money from chain A to chain B.
[681.9s] And really the only way to make that stuff work is you have to go back to ZK.
[684.9s] So ZK is overly complicated, but it is necessary.
[690.0s] And so...
[694.5s] We started looking at that again, but I think like the safe thing to do is start with a proven technology and Zcash had been around for years and nobody had stolen money.
[705.4s] And this is just sort of like a subset of ZK, but it's kind of a cool thing.
[710.1s] You can build what they call tumblers of money.
[713.0s] You throw a bunch of money in and then...
[716.2s] the money that you put into the Tumblr is, you know how much went in, but the ownership is completely scrambled up.
[725.3s] And at any time you can go and transfer money from within the Tumblr from one user to another, but only the users who did the transferring and got the money know what was there, but nobody else can see what's happening.
[737.4s] So again, like you have these systems of multiple users with lots of money, but you don't know who owns a percentage of the money.

**SPEAKER_01:**
[745.5s] Yeah, actually, before we even go that far, can we talk just like, what is ZK and how does it work and why is it an important part of the solution?

**SPEAKER_03:**
[754.0s] I want to pull back for also a second.
[757.7s] I remember, I think there was an Ethereum meetup in New York.
[760.9s] I'm not sure if either of you guys were there.
[763.1s] I think I spoke at it, maybe.
[768.4s] was also a zcash i think presentation there and it was at that time taking seven minutes to generate the zk proofs so yes you wanted to make a transaction you like did this thing it took seven minutes and then the verification was kind of fast so once you had it and you sent it to the network things could go on you know but the uh
[791.3s] The usability was not there in those days.
[793.5s] This is part of the reason we weren't like going to tell our enterprise customers like, oh, yeah, let's let's ZK everything.
[800.1s] You know, even if we had it all integrated nicely, there's a lot of devil in the details.
[804.3s] And it was unbelievably slow for a while.
[806.4s] And I think it's fixed.

**SPEAKER_02:**
[807.4s] But yeah, well, it's complicated.
[810.2s] I mean, what I was trying to say before is like I have like sort of nuts and bolts experience of what's going on in Zcash.
[817.6s] But the more complicated world of zero knowledge, that's my aspirational part right now.
[824.6s] I can sort of see pieces moving within there, but would hesitate to speak more broadly on this.
[833.3s] Except I'll say that it is more complicated than any of the, like, for instance, Ethereum client implementation stuff.

**SPEAKER_01:**
[844.5s] Yeah, can you give a high-level summary of what zero knowledge is?
[848.6s] Like, I think very few people understand.

**SPEAKER_03:**
[851.0s] I have a good layman example, I think, and Jim can correct me.
[856.2s] So I did once take a theoretical cryptography class, and the example they bring up is the CEO problem, so to speak.
[865.1s] So you've got two CEOs, and they're high ego guys, you know.
[870.1s] And they want to know... Do you say that from experience, Karen?
[876.5s] I'm not speaking about myself.
[879.5s] They want to know who has the most between the two.
[884.8s] But they don't want to know how much money.
[886.9s] They merely want to know...
[890.0s] uh which one has more and you would think that there wouldn't really be a way to create a scheme in which they could learn that information and nothing else but there actually is um
[906.8s] And again, this is almost 10 years ago now, so I may be describing the example incorrectly.
[911.9s] But yeah, that's like a case where you might want zero knowledge.
[916.5s] Similarly, like an ID check at a bar.
[920.4s] You're leaking all your personal info when you hand the ID to the bouncer, to your home address, your full name, your date of birth, et cetera.
[929.6s] So you might want to prove to the bar that you're over 21
[933.3s] without handing any other info over, basically.
[936.9s] So I think this is the general setting that it ends up at.
[940.7s] Jim, do you want to take that and run with it, correct it?

**SPEAKER_02:**
[946.3s] Yeah, so when you first look up zero knowledge, there are lots of little examples like this that are all pretty cool.
[954.9s] And what's really happening in Zcash is that what you're trying to do is...
[961.8s] pass money from person A to person B, and person A wants to prove to person B that they have the money and that it was actually transferred, but without giving away the amount of money that person A has, or without person A learning how much that person B has, just that you know that the state before was that you had the amount, and that the state after is that it was transferred over.
[983.5s] And then also no one else in the world can know this.
[987.0s] So you're proving sort of the important parts, but not others.
[990.5s] Zero knowledge could get
[992.2s] Pretty complicated too, because when you start looking into it, there are a lot of one-off examples like you're talking about that you can sort of see a solution to.
[1000.5s] But the problem comes about in trying to come up with sort of a generic solution where you can almost just compile any amount of code into some ZK proof and then run that for anything.
[1014.1s] I don't remember because it's been about a year now, but in zero cache, there were multiple zero knowledge proofs in there.
[1022.1s] for various aspects.
[1023.9s] I might be making up some of the details here, but I think there was like one proof was like to show that you had more than such and such money before the transfer.
[1032.9s] I might have it slightly off, but there were multiple of these zero knowledge algorithms in there, but put together, they allowed for the full sort of transfer of money within the Tumblr.
[1047.6s] And each one sort of had been worked out independently of each other.
[1051.6s] using a more generic system where they compiled certain algorithms in there.

**SPEAKER_03:**
[1058.9s] If that makes sense.

**SPEAKER_02:**
[1059.8s] So making it generic can get really complicated.

**SPEAKER_03:**
[1063.1s] Terminology for the listener that you may have heard that I barely remember.
[1067.4s] So snarks and starks were a thing that Vitalik was talking about a lot and still does.
[1076.3s] So it's like succinct, non-interactive.
[1080.7s] arbitrary something computation i can't remember like but basically interactive proof yes but what's the whole acronym but so there is a way i think to take an arbitrary computation and to prove that it has a certain result without revealing like the intermediate states and so on but it's not computationally feasible like or it's just so slow that if you try to do it that way
[1110.4s] it becomes very difficult.
[1113.2s] So I believe, just tying back to Jim's point, you could try to do this in a generality, like the EVM.
[1119.8s] I can verify, there are these ZK EVMs.
[1122.2s] I can verify any computation that comes out of this thing.
[1124.9s] And I think the problem with them has been performance.
[1128.3s] And so the Zcash people, I guess, had to decompose every little step into specific circuits, right?
[1139.5s] Yeah.
[1140.4s] It's very low-level programming thinking in the ZK world.
[1146.7s] Literally, they're circuits that you end up compiling and so on and so forth.

**SPEAKER_00:**
[1153.4s] So yeah, Zcash at the moment is onto its feet.

**SPEAKER_02:**
[1156.2s] And sort of by identifying a certain set of algorithms and just focusing on them, they were able to sort of solve this one Tumblr problem without going any more in-depth than that.
[1166.4s] So this isn't like...
[1167.8s] Like in the dream world, you would take any Ethereum contract and compile it somehow as something zero knowledge and then prove that you had run the full contract.
[1182.0s] That's something that at the time, at least so far in the world as it is, I didn't want to get into it or have us get into it as a company.
[1191.5s] But just to have these tumblers in place, I think that solves a lot of problems.

**SPEAKER_01:**
[1196.2s] Yeah, Bob, you were saying something?

**SPEAKER_00:**
[1198.1s] Yeah, so Zcash is onto its fourth round of different cryptography.
[1203.9s] So I forget what they're called, Sapling, something else.
[1207.1s] We're onto Orchard now.
[1209.9s] But I mean, that's been now over the course of nearly a decade.
[1215.0s] You know, each time you've got another sort of two years worth of leading edge advancement.
[1222.2s] And...
[1223.8s] and yeah like talking about that performance thing so something which i think has been a a key piece in uh in zcash price appreciation recently has been the arrival of a functional mobile wallet so that's called zashi which is made by the uh
[1243.8s] electric coin company but you're basically at the point where you can run that proof on your phone so something which used to be laptop seven minutes is now phone second um so what you've seen if you look at the size of these shielding pools where these pools are effectively like you know all of these things are all
[1270.1s] you know mixed and hidden together right the more that you've got in a pool the more uh you know and the more unlinkable you are if you have a you know if you if you do something simple like ring signatures where you just whatever sick i think monero's got 16 transactions that that you know get all joined together so you can trace through that
[1296.1s] to a degree, but if you've got hundreds or thousands or millions of people in that same pool, it's effectively completely anonymous at that point.
[1310.1s] But if you look at the stats of usage
[1313.4s] of these particular pools are you seeing what proportion of the money supply has been shielded versus being transparent i guess this is another thing to say right is is bitcoin is transparent you know so same same with ethereum but then they they use the world word shielded to talk about you know that you are within this anonymity set
[1339.6s] these earlier rounds you know you had a bit of use but not a ton of use um but right now i can't find the view but it but it was something like about four or five million of the 21 million were within that shielding pool so you know a significant chunk of it is shielded now which was never the case in the past you know um
[1366.6s] I remember on ETC at some point, we were looking at whether we were going to bring over the precompiles to do with some of the curves.
[1374.0s] I don't know if you remember that happened in Ethereum at some point, but one of the Blake curves, I think, went into the precompile.
[1381.5s] And we were talking about whether we were going to do that or not.
[1385.5s] And really talking about gas limit as well.
[1389.1s] How gas expensive would operations be using these things even?
[1395.0s] the stats at that time were you know it's like maybe two percent of transactions on zcash were shielded something like that you know it's basically like not being used at all you know functionally pretty much identical to bitcoin but probably a lot of end users going yeah i'm using zcash i'm private it's like yeah you know you're not not at all you're getting zero benefit at all
[1421.1s] But yeah, that's really happening now.
[1424.1s] And I think it's just, you know, these rounds and rounds and years and years of research and then implementation of those and engineering effort.
[1431.7s] And it's like, hey, it works now.

**SPEAKER_01:**
[1436.8s] Well, from your standpoint, Jim, like, is it a technological advancement that Zcash has created?
[1443.9s] Or is it just simply that these tumblers have gotten big enough that they offer real privacy?
[1449.8s] Do you know what I mean?

**SPEAKER_02:**
[1454.0s] I mean, any of these things are technological advancements.
[1459.0s] But, I mean, you want to have the tumblers big enough so that you have some amount of anonymity within there.
[1467.1s] If it's a tumbler of one person, then it's not much of a tumbler.

**SPEAKER_03:**
[1473.2s] I need to interject.
[1475.2s] I have a crypto friend who was texting about 30 seconds ago about whether I like Zcash at this price.
[1483.1s] This is a prerecorded podcast, so I guess it'll run on Wednesday, November the 12th.
[1491.1s] But very timely.
[1494.4s] it's sort of like i again there's the old crypto joke where like when your dentist and realtor friends start asking you about ripple and cardano it's time to unwind your positions a little bit you know but it's the zcash meta i don't know like maybe that means there's room to run maybe uh maybe it's tops but uh well as they say it's like catching a falling knife right like you know trying to figure out the peak of the market

**SPEAKER_01:**
[1522.4s] Okay, we've talked about kind of how Zcatch works, and it uses ZK in these sort of very specific areas, and it's not programmable generally.
[1535.2s] Now, obviously, there's a lot of talk in the Ethereum world about ZK EVMs.
[1540.9s] Do you guys have any thoughts on that and how those work?
[1544.4s] Because at what point do we get...
[1549.7s] Is it truly impossible to get full programmability or is that something that is just getting closer?

**SPEAKER_03:**
[1557.4s] From a market perspective, I think they're mostly ZK AVMs have been used for scaling as opposed to privacy.
[1566.8s] Even there, you tend to see some amount of specificity.
[1569.8s] Like I think I mentioned on a podcast before, I'm friend acquaintances with the Leiter CEO and Leiter uses
[1580.2s] lighters like the L2 version of Hyperliquid, if you will, where they do perps and they do zero knowledge matching off-chain, but you know it actually works and it gets written to Ethereum, which is pretty cool.
[1593.6s] And supposedly they're achieving really high throughputs this way.
[1595.7s] It's not necessarily privacy tech at all.
[1601.2s] ran into some of the aztec folks in singapore and it seems trending general purpose still on testnet um but not full evm it's like a restricted utxo type language of sorts i believe um so i think there's probably not being nearly as expert as jim who i'll defer to in a second uh not being an expert i think it will be there's no intrinsic reason you can't make it
[1631.4s] full EVM or full Rust or JavaScript or whatever, but probably there will be a tremendous amount of optimization that would have to happen to make that happen.
[1644.5s] So you probably see special purpose for a while.

**SPEAKER_00:**
[1648.3s] I saw that, and now I'm blanking on the name, the ZK tech that was happening under the Polygon.
[1658.4s] banner um with uh jordi uh bailina um and i can't remember the the name of the project now they posted within the last few months that they were real-time zk proving mainnet now um but you know it was with a battery of of gpus it was not a thing that you would be doing yourself but but yeah that that full proving is you know is
[1688.9s] possible but yeah you you have that optimization to to be done but i mean i think i think that's where things are going to end up that you've had this um sort of
[1704.0s] improvement where starting at bitcoin it's like well how are we going to prove you know get to global consensus and and solve the double spend problem well it it's by publishing all the details and then we're gonna have you know uh redundant um state machines running in parallel right and that's that's the answer we know that works it was like what you know you know like satoshi did the big ugly thing
[1733.5s] but it worked and it made this stuff possible that had never been possible before.
[1738.2s] But it is, you know, it's an incredibly big, ugly, expensive way of doing that.
[1744.2s] And then I think just over time, it's like, okay, well...
[1749.2s] having things public was sort of a requirement for that consensus model but that was never intentional like having them all as a public ledger like that that's not a positive feature now if you look at the cypherpunk um culture that many of these people were coming out of yeah it's it's private unstoppable money like yeah no it wouldn't be public so i saw that uh yeah within weeks
[1778.3s] of Bitcoin starting, Hal Finney said, you know, looking at ways of improving anonymity in Bitcoin.
[1786.7s] So that was January 2009.
[1789.0s] You know, that was a cypherpunk's obvious first reaction is, yeah, this is cool now.
[1795.6s] But yeah, we should have privacy as well.
[1798.4s] And I think we're sort of getting to that point of the tech has become good enough to to solve that without broadcasting everything to everyone.

**SPEAKER_01:**
[1809.4s] Yeah, Jim, what do you think, like, you know, on the sort of general programmability ZK front?

**SPEAKER_02:**
[1816.6s] I wish I had more, you know, hands-on experience with general ZK.
[1823.4s] I see a lot of people very excited by it.
[1827.2s] And maybe in a way that makes me skeptical because it seems like a cool toy.
[1834.0s] But I am open to them working great.
[1836.9s] And so I don't want to make a strong, firm stance at the moment on them, but they would be great if they were.

**SPEAKER_01:**
[1848.1s] Yeah, it seems like the approach to Karen's point is like find specific areas where you can create circuits and apply them and optimize for those and then expand that over time.
[1860.8s] You know, like it's really about kind of like
[1863.8s] you know, nailing those initial use cases.

**SPEAKER_02:**
[1865.9s] And that's why I was drawn to that.
[1870.4s] Because if you really narrow it down to something really simple, then I think you can do it well.

**SPEAKER_03:**
[1877.7s] I've heard that people even maybe compile the specific circuits and then optimize.
[1883.3s] Like you kind of write them with the general tool.
[1885.4s] Some people do.
[1886.6s] I don't know.
[1887.3s] And then you kind of like, okay, I got the circuit for the specific thing, but then I got to make it like work.
[1893.1s] Yeah.

**SPEAKER_01:**
[1895.5s] I think compiling a circuit is still pretty very computational intensive, but it's way less.
[1903.8s] For most circuits, once a circuit is compiled, it's way less to do the proof.
[1909.2s] You got to continue to push that down, but I think the ratio is very large.
[1916.7s] Well, I think we are at time.
[1920.2s] You know, where can we find you, Jim?
[1922.6s] I'm going to start with you.
[1926.2s] Where can you find me?
[1927.6s] Yes.
[1928.3s] If you want to hear more and learn more about Jim, which I, you know, please speak up, ask him where can, where they find you.

**SPEAKER_02:**
[1937.4s] I do have a Twitter handle.
[1938.4s] What is my Twitter handle?
[1939.3s] I can't remember, but probably.

**SPEAKER_01:**
[1942.4s] I guess it's jam sheet probably.

**SPEAKER_03:**
[1945.0s] I'm going to try to check.
[1946.1s] Hold on.
[1946.9s] Yeah.

**SPEAKER_01:**
[1949.2s] But whatever it is, you should post more often.

**SPEAKER_02:**
[1954.2s] I like wake up one day and remember that Twitter exists, and then I tweet a lot, and then I forget about it for a couple of weeks.

**SPEAKER_01:**
[1961.1s] Sorry, it's Jay from us, like J-H-O-Y.

**SPEAKER_03:**
[1963.6s] I threw it in the chat.
[1965.2s] I don't know if we can all see that, the studio chat.

**SPEAKER_01:**
[1968.9s] Yeah.
[1970.0s] So, yes.
[1972.2s] You can find him at Jay Hermos.
[1974.1s] Karen, where can people find you?

**SPEAKER_03:**
[1975.3s] Jamshied Hermos.

**SPEAKER_01:**
[1976.6s] Oh, Jamshied Hermos.

**SPEAKER_03:**
[1978.5s] Yeah, I'm on X, K, James Lubin.
[1981.8s] I'm also on Substack, trying to, you know, I have like a couple old Medium posts that I've linked from there.
[1989.1s] I'm getting a little bit into a Substack rhythm.
[1992.0s] It'll probably be infrequent, but at least of moderate to high quality.
[1996.7s] Also, K, James Lubin.
[1998.6s] um, dot sub stack.
[2000.5s] I think for now, maybe I'll change the URL, uh, and link it to me in the show notes when we start assuming we do show notes.

**SPEAKER_01:**
[2010.1s] And you can find me on X at Vic for Wong.
[2013.8s] Um,
[2014.1s] Bob has posted why I explained before in my handle.
[2018.1s] You can also find us on Telegram at the Strong Mercada group.
[2022.8s] Just go to our website at strongmercada.com and that will point you to Telegram.
[2028.6s] And Bob, where can people find you and what can people expect next week?

**SPEAKER_03:**
[2031.8s] Don't close it out.
[2032.9s] Bob, you're the resident Zcash shill.
[2035.9s] One year from now, Zcash price or market cap or both?

**SPEAKER_00:**
[2040.9s] I think it will be in the top 10.
[2044.0s] Top 10?
[2045.0s] It's been very close.
[2047.2s] And the primary reason is privacy is a big need, and it's solved it, right?
[2054.2s] It's not some future promise.
[2055.8s] Like, it works right now.
[2056.9s] There's a mobile app.
[2057.8s] People are using it.
[2058.8s] You know, you've got like a 10-year, near 10-year history of...
[2063.5s] you know top brainiacs working on this lots of credibility so you know i i think it it's great and then i'm looking forward to smart contracts with with that kind of level as well just one more thing to mention i couldn't remember geordie's project zisk
[2082.9s] So that's a spin-off group now from Polygon, led by Jordi Bailina, and they announced real-time proving of mainnet blocks.
[2094.3s] That was announced at FCC this year.
[2097.8s] So proving a block...
[2101.6s] in seven and a half to 12 seconds so just under block time however it requires 24 very high powered gpus or 48 more consumer spec so you've got a rack there you go and bob with that prediction where can we find you and can you give us a preview of what people can expect next week
[2128.3s] Absolutely, yes.
[2129.1s] So I'm Bob Summerwill, Summer like the season, W-I-L-L.
[2135.3s] So on everything with that name.
[2138.8s] And yes, so next week, we will have an early days of Ethereum interview with Christoph Jentz, formerly of...
[2148.5s] of fdev so he was hired in september 2014 into that berlin office uh worked on uh testing cross-line testing um and then later on slockit with their smart locks and the creation of the dow which is probably uh you know ethereum's first killer app until the killing killing in many different ways yes

**SPEAKER_01:**
[2176.3s] Or you can say birthing because ETC came out of that.
[2179.6s] Correct.
[2180.4s] Right.
[2181.8s] Okay.
[2182.2s] Well, that's time.
[2183.4s] Thank you very much for joining us.
[2185.1s] And we look forward to seeing you next week.
[2187.1s] Take care.

**SPEAKER_00:**
[2188.0s] Thanks, everybody.
