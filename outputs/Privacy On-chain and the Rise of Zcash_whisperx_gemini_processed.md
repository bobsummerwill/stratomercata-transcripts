SPEAKER_01:**
[00:01] Okay, welcome everyone.
[00:03] We have a very special and very timely topic today: privacy on-chain and the rise of Zcash.
[00:08] And we sort of have a special guest today.
[00:10] So I'm Victor Wong.
[00:11] I am founder and chief product officer at BlockApps.
[00:14] I'll get to our normal guests, but today we have Jim.
[00:16] Do you want to give us a quick intro?

**SPEAKER_02:**
[00:18] Yeah, I'm also—I've known Victor and Kieran for years.
[00:21] I'm one of the founders of BlockApps and CTO.

**SPEAKER_01:**
[00:23] And you're here in particularly because I would call you a Zcash expert, having written your own Zcash client.

**SPEAKER_02:**
[00:28] Well, I think I'm more aspirational at this point in time.
[00:31] I mean, the way I learn about things is I try to...

**SPEAKER_03:**
[00:33] How many more expert people do you think there are on, say, Zcash in particular on the planet?

**SPEAKER_02:**
[00:38] No, the problem that I have is that I was sort of halfway in the learning process last year.
[00:42] So the way I learn about things is I try to, like, write a client for it.
[00:45] So I was doing that, but then we got pulled in different directions.
[00:48] I got to the point where I had sort of replicated the actual client that could connect.
[00:51] It would bring the data in.
[00:52] It would bring the proofs in.
[00:54] But just about when I was getting to the good part, that's when we moved on to other things.

**SPEAKER_03:**
[00:58] Well, we're going to put the number...
[00:59] I'll answer my own question: right between, like, 10 and 100, maybe.
[01:03] I would say there are definitely less than 20 people who have written their own Zcash clients, probably.
[01:07] Well, yeah, there's probably some core contributors.
[01:09] I imagine there's more than a handful into Zcash, but you know, when Jim says non-expert, you know, it's like there are, let's say... yes.
[01:15] I'll expand the range.
[01:16] Five to 100 people who understand Zcash better on the planet.
[01:20] Big, big, big range there.
[01:21] But we're talking about pretty small numbers in absolute terms.
[01:24] Yes, exactly.

**SPEAKER_01:**
[01:25] I would say if Jim's not an expert, I don't know what even "expert" means.
[01:29] Anyways, Kieran, do you want to give a quick intro of yourself?

**SPEAKER_03:**
[01:31] Certainly.
[01:32] Um, I'm our CEO. I've been on these before.
[01:34] By the way, Vic, you're letting Jim off the hook calling him a special guest.
[01:37] He has to do this all the time now with our, you know, continued... in the public.
[01:40] So, special in the future. Special today. Today is special, but it's the first of many, let's just say that.
[01:45] I was looking through the prior videos. Jim has never appeared on one of our own spaces.

**SPEAKER_00:**
[01:49] He's only been on Early Days of Ethereum.

**SPEAKER_03:**
[01:51] Okay.

**SPEAKER_01:**
[01:52] There you go.
[01:52] But it won't be special soon.
[01:54] Bob, by the way, since you've spoken up, can you give a quick intro to yourself?

**SPEAKER_00:**
[01:58] So hi, I'm Bob.
[01:59] I'm Head of Ecosystem.
[02:01] And yeah, been doing a lot of spaces.

**SPEAKER_01:**
[02:03] Yeah.
[02:04] So I think, you know, to level set, because I think there's a lot of...
[02:07] misunderstanding about what privacy is.
[02:09] How would you define blockchain privacy and why do you think it's important?

**SPEAKER_00:**
[02:13] Who's that question for?

**SPEAKER_01:**
[02:14] Could be for anyone, whoever wants to go.
[02:16] Kieran, you want to kick us off?

**SPEAKER_03:**
[02:17] So, and for the—I assume that the viewer is pretty deep in the space, but I'll bring it down to a fairly low technical level.
[02:23] So blockchains are great.
[02:24] They let you move digitally scarce value from party to party.
[02:28] And the... way that this is typically done is that you've got a big address which is almost, but not quite, a public key.
[02:34] And you sort of sign a message that says, "I, Kieran"—but it's not Kieran because it's this address—"send, you know, three Bitcoin to Bob."
[02:40] And it doesn't say Bob; it's another address.
[02:42] You don't quite know who either of those parties are. However, you've got the address forever.
[02:47] And often it is the case that you can piece together what happens based on that address.
[02:51] So say you're on a centralized exchange which has KYC.
[02:54] It knows how to associate you to maybe a withdrawal address.
[02:57] It may not know down the line.
[02:59] But if you start to get a bunch of data points, you can kind of piece together who sent what to whom.
[03:04] And you're actually in an extremely transparent scenario where everyone's financial transactions are visible to everyone.
[03:10] And it's not—while it's a cryptographic technology, it's not necessarily a private technology.
[03:15] And this has been a problem both in the consumer setting, just for, you know, people don't like this.
[03:19] Satoshi makes a comment, I believe in the white paper, saying that,
[03:23] you know, obviously to prevent the double-spend problem—which basically just is just that, to ensure that Bitcoin can't be created or destroyed except by the agreed mechanism—obviously you need to know the whole history.
[03:32] And so he sees the problem as intrinsic, but some technologies came out later that maybe call that into question that we'll talk about.
[03:38] It's also an enterprise problem.
[03:40] So we can talk separately about our experience there.
[03:43] Sort of what the enterprises want is kind of the same as what the public blockchain people want, except with selective visibility.
[03:49] So they want to say, you're doing like an on-chain stock trade, which is actually now starting to happen.
[03:54] You sort of want to know the other party has the stock.
[03:56] You don't necessarily want to know who the other party is.
[03:59] But you want to know that they acquired that stock legitimately.
[04:02] And then when you get it, you want to be able to pass it on legitimately in the same way.
[04:06] And then there's sometimes this extra requirement that, like, the regulator can see everything, you know?
[04:10] So you want sort of like a unlinkability of balance to person or company, but also this mass preservation property that I was talking about: can't create or destroy assets.
[04:18] They have to be acquired legitimately, and so on.
[04:21] So it's a perennial problem and closer to solved, you know, but we can go into that shortly.

**SPEAKER_01:**
[04:26] Yeah.
[04:26] Bob, did you want to add anything to that?

**SPEAKER_00:**
[04:28] Yeah.
[04:28] Yes.
[04:29] I mean, going back to those Bitcoin, you know, beginnings in the Bitcoin white paper, you know, it just talks about severing identity from transactions.
[04:36] But really, that's just pseudonymous, not anonymous.
[04:39] And I think a lot of people didn't understand that differentiation back in those early days.
[04:43] And it's like, "Oh, Bitcoin's private, untrackable, you know, digital money."
[04:48] But, you know, very rapidly you have blockchain analytics coming in, you know, looking for correlations and patterns.
[04:54] And it's like, yeah, that's... you're not getting a lot of security.
[04:57] You know, even if you're not reusing addresses, just sort of normal things that people would do, there's lots of correlations and, you know, you can get unmasked that way.
[05:04] But yeah, Satoshi did talk a bit about zero-knowledge.
[05:06] I can't remember who raised it.
[05:08] Somebody raised it early and he was like, "Yeah, that would be interesting if we could do that."
[05:11] But it was just like a lot of that cryptography just hadn't happened.
[05:14] So Zcash started in 2016, and it was only around that kind of time or a little before that you started having these papers on SNARK constructions and going through all these different kind of rounds.
[05:24] So, yeah, I mean, what that's meant is Bitcoin and then Ethereum following that same path.
[05:29] You know, they are an immutable public ledger forever.
[05:32] Ethereum even worse because it's an account model.
[05:35] So you are reusing the addresses all the time, right?
[05:37] And if your address is unmasked, you are forever doxxed.
[05:41] That's happened to at least one of the Ethereum founders who moved hundreds of millions of dollars out of a known address of his, which probably not desired.

**SPEAKER_01:**
[05:49] And I, you know, you guys have been talking about Satoshi, but Jim, I remember, I think it's like earlier, like 2014, Vitalik was talking like, he was like, ZK-SNARKs will fix all of this at some point in time.
[05:59] Do you remember that at all?

**SPEAKER_02:**
[06:00] Well, I mean, like, I think we went through a learning process about privacy and that's sort of like, we're understating this right now.
[06:06] Maybe it's because we put a lot of time and effort into some privacy solutions that, you know,
[06:10] technically worked, but were a business failure, I think is fair to say.
[06:14] And so, you know, the audience can learn from our, like, sort of failed mistakes in the past right now.
[06:19] But we sort of built... so we had heard years ago about ZK, but we sort of just, I don't know, at the time looked into it and said like, "Oh, this looks like overly complicated.
[06:27] You can get privacy through these other means."
[06:29] And we ended up building a system that
[06:32] allowed for sort of like quick spin-up of private chains that everything was sort of like in an encrypted tunnel and you could have like these chains completely secure and nobody else would see what was happening there.
[06:41] But long story short, you know, slow learning process.
[06:44] We found out that customers want everything and
[06:47] to the point that it made it worthless.
[06:49] Like we would go into enterprise, we would say like, "Oh, you can set up these private channels with others."
[06:53] And they loved that because they could sort of control that and they could control who goes in there.
[06:57] But then once everything was going through these private channels, then they wanted to be able to like transfer from private chain to private chain.
[07:03] And that's where everything started to fall apart.
[07:05] And getting things back onto the main chain became sort of this extra complicated system.
[07:10] And at the same time, customers wanted to have like a full flexibility in having like extensions to Solidity where you could just like name a chain and send some money from chain A to chain B.
[07:18] And really the only way to make that stuff work is you have to go back to ZK.
[07:22] So ZK is overly complicated, but it is necessary.
[07:25] And so... we started looking at that again, but I think like the safe thing to do is start with a proven technology, and Zcash had been around for years and nobody had stolen money.
[07:34] And this is just sort of like a subset of ZK, but it's kind of a cool thing.
[07:37] You can build what they call tumblers of money.
[07:40] You throw a bunch of money in and then...
[07:42] the money that you put into the tumbler is, you know how much went in, but the ownership is completely scrambled up.
[07:47] And at any time you can go and transfer money from within the tumbler from one user to another, but only the users who did the transferring and got the money know what was there, but nobody else can see what's happening.
[07:56] So again, like you have these systems of multiple users with lots of money, but you don't know who owns a percentage of the money.

**SPEAKER_01:**
[08:02] Yeah, actually, before we even go that far, can we talk just like, what is ZK and how does it work and why is it an important part of the solution?

**SPEAKER_03:**
[08:09] I want to pull back for also a second.
[08:11] I remember, I think there was an Ethereum meetup in New York.
[08:14] I'm not sure if either of you guys were there.
[08:15] I think I spoke at it, maybe.
[08:17] There was also a Zcash, I think, presentation there and it was at that time taking seven minutes to generate the ZK proofs.
[08:23] So yes, you wanted to make a transaction, you like did this thing, it took seven minutes, and then the verification was kind of fast.
[08:29] So once you had it and you sent it to the network, things could go on, you know, but the...
[08:33] the usability was not there in those days.
[08:35] This is part of the reason we weren't like going to tell our enterprise customers like, "Oh, yeah, let's let's ZK everything."
[08:41] You know, even if we had it all integrated nicely, there's a lot of devil in the details.
[08:45] And it was unbelievably slow for a while.
[08:48] And I think it's fixed.

**SPEAKER_02:**
[08:49] But yeah, well, it's complicated.
[08:51] I mean, what I was trying to say before is like I have like sort of nuts and bolts experience of what's going on in Zcash.
[08:57] But the more complicated world of zero-knowledge, that's my aspirational part right now.
[09:01] I can sort of see pieces moving within there, but would hesitate to speak more broadly on this.
[09:06] Except I'll say that it is more complicated than any of the, like, for instance, Ethereum client implementation stuff.

**SPEAKER_01:**
[09:12] Yeah, can you give a high-level summary of what zero-knowledge is?
[09:15] Like, I think very few people understand.

**SPEAKER_03:**
[09:17] I have a good layman example, I think, and Jim can correct me.
[09:20] So I did once take a theoretical cryptography class, and the example they bring up is the CEO problem, so to speak.
[09:26] So you've got two CEOs, and they're high ego guys, you know.
[09:29] And they want to know... (Do you say that from experience, Kieran?)
[09:32] I'm not speaking about myself.
[09:34] They want to know who has the most between the two.
[09:37] But they don't want to know how much money.
[09:39] They merely want to know
[09:41] which one has more.
[09:43] And you would think that there wouldn't really be a way to create a scheme in which they could learn that information and nothing else, but there actually is.
[09:50] And again, this is almost 10 years ago now, so I may be describing the example incorrectly.
[09:55] But yeah, that's like a case where you might want zero-knowledge.
[09:58] Similarly, like an ID check at a bar.
[10:01] You're leaking all your personal info when you hand the ID to the bouncer: your home address, your full name, your date of birth, et cetera.
[10:07] So you might want to prove to the bar that you're over 21
[10:11] without handing any other info over, basically.
[10:13] So I think this is the general setting that it ends up at.
[10:16] Jim, do you want to take that and run with it, correct it?

**SPEAKER_02:**
[10:18] Yeah, so when you first look up zero-knowledge, there are lots of little examples like this that are all pretty cool.
[10:24] And what's really happening in Zcash is that what you're trying to do is...
[10:28] pass money from person A to person B, and person A wants to prove to person B that they have the money and that it was actually transferred, but without giving away the amount of money that person A has, or without person A learning how much that person B has, just that you know that the state before was that you had the amount, and that the state after is that it was transferred over.
[10:45] And then also no one else in the world can know this.
[10:47] So you're proving sort of the important parts, but not others.
[10:50] Zero-knowledge could get
[10:52] pretty complicated too, because when you start looking into it, there are a lot of one-off examples like you're talking about that you can sort of see a solution to.
[10:58] But the problem comes about in trying to come up with sort of a generic solution where you can almost just compile any amount of code into some ZK proof and then run that for anything.
[11:08] I don't remember because it's been about a year now, but in Zcash, there were multiple zero-knowledge proofs in there
[11:14] for various aspects.
[11:15] I might be making up some of the details here, but I think there was like one proof was like to show that you had more than such and such money before the transfer.
[11:22] I might have it slightly off, but there were multiple of these zero-knowledge algorithms in there, but put together, they allowed for the full sort of transfer of money within the tumbler.
[11:31] And each one sort of had been worked out independently of each other,
[11:35] using a more generic system where they compiled certain algorithms in there.

**SPEAKER_03:**
[11:38] If that makes sense.

**SPEAKER_02:**
[11:39] So making it generic can get really complicated.

**SPEAKER_03:**
[11:41] Terminology for the listener that you may have heard that I barely remember.
[11:44] So SNARKs and STARKs were a thing that Vitalik was talking about a lot and still does.
[11:49] So it's like succinct, non-interactive,
[11:53] arbitrary something computation... I can't remember, like... interactive proof, yes, but what's the whole acronym?
[11:57] But so there is a way, I think, to take an arbitrary computation and to prove that it has a certain result without revealing like the intermediate states and so on, but it's not computationally feasible, or it's just so slow that if you try to do it that way,
[12:08] it becomes very difficult.
[12:10] So I believe, just tying back to Jim's point, you could try to do this in a generality, like the EVM.
[12:15] I can verify—there are these ZK-EVMs—I can verify any computation that comes out of this thing.
[12:20] And I think the problem with them has been performance.
[12:22] And so the Zcash people, I guess, had to decompose every little step into specific circuits, right?
[12:27] Yeah.
[12:28] It's very low-level programming thinking in the ZK world.
[12:31] Literally, they're circuits that you end up compiling and so on and so forth.

**SPEAKER_00:**
[12:35] So yeah, Zcash at the moment is onto its...

**SPEAKER_02:**
[12:36] And sort of by identifying a certain set of algorithms and just focusing on them, they were able to sort of solve this one tumbler problem without going any more in-depth than that.
[12:45] So this isn't like...
[12:46] like in the dream world, you would take any Ethereum contract and compile it somehow as something zero-knowledge and then prove that you had run the full contract.
[12:54] That's something that at the time, at least so far in the world as it is, I didn't want to get into it or have us get into it as a company.
[13:00] But just to have these tumblers in place, I think that solves a lot of problems.

**SPEAKER_01:**
[13:04] Yeah, Bob, you were saying something?

**SPEAKER_00:**
[13:05] Yeah, so Zcash is onto its fourth round of different cryptography.
[13:09] So I forget what they're called, Sapling, something else.
[13:12] We're onto Orchard now.
[13:13] But I mean, that's been now over the course of nearly a decade.
[13:16] You know, each time you've got another sort of two years' worth of leading-edge advancement.
[13:20] And... and yeah, like talking about that performance thing, so something which I think has been a key piece in Zcash price appreciation recently has been the arrival of a functional mobile wallet.
[13:30] So that's called Zashi, which is made by the
[13:33] Electric Coin Company, but you're basically at the point where you can run that proof on your phone.
[13:38] So something which used to be laptop, seven minutes, is now phone, one second.
[13:42] Um, so what you've seen, if you look at the size of these shielding pools, where these pools are effectively like, you know, all of these things are all,
[13:50] you know, mixed and hidden together, right?
[13:52] The more that you've got in a pool, the more, you know, and the more unlinkable you are.
[13:56] If you have a, you know, if you do something simple like ring signatures where you just whatever, I think Monero's got 16 transactions that get all joined together.
[14:05] So you can trace through that
[14:07] to a degree, but if you've got hundreds or thousands or millions of people in that same pool, it's effectively completely anonymous at that point.
[14:14] But if you look at the stats of usage
[14:17] of these particular pools, or you're seeing what proportion of the money supply has been shielded versus being transparent—I guess this is another thing to say, right, is Bitcoin is transparent, you know, so same with Ethereum.
[14:27] But then they use the word "shielded" to talk about, you know, that you are within this anonymity set.
[14:32] These earlier rounds, you know, you had a bit of use, but not a ton of use.
[14:35] But right now, I can't find the view, but it was something like about four or five million of the 21 million were within that shielding pool.
[14:43] So, you know, a significant chunk of it is shielded now, which was never the case in the past, you know.
[14:48] I remember on ETC at some point, we were looking at whether we were going to bring over the precompiles to do with some of the curves.
[14:54] I don't know if you remember that happened in Ethereum at some point, but one of the BLAKE curves, I think, went into the precompile.
[15:00] And we were talking about whether we were going to do that or not.
[15:02] And really talking about gas limit as well.
[15:04] How gas expensive would operations be using these things even?
[15:08] The stats at that time were, you know, it's like maybe 2% of transactions on Zcash were shielded, something like that.
[15:14] You know, it's basically like not being used at all, you know, functionally pretty much identical to Bitcoin.
[15:19] But probably a lot of end users going, "Yeah, I'm using Zcash, I'm private."
[15:22] It's like, yeah, you know, you're not. Not at all. You're getting zero benefit at all.
[15:26] But yeah, that's really happening now.
[15:28] And I think it's just, you know, these rounds and rounds and years and years of research and then implementation of those and engineering effort.
[15:35] And it's like, "Hey, it works now."

**SPEAKER_01:**
[15:36] Well, from your standpoint, Jim, like, is it a technological advancement that Zcash has created?
[15:41] Or is it just simply that these tumblers have gotten big enough that they offer real privacy?
[15:46] Do you know what I mean?

**SPEAKER_02:**
[15:47] I mean, any of these things are technological advancements.
[15:50] But, I mean, you want to have the tumblers big enough so that you have some amount of anonymity within there.
[15:55] If it's a tumbler of one person, then it's not much of a tumbler.

**SPEAKER_03:**
[15:58] I need to interject.
[15:59] I have a crypto friend who was texting about 30 seconds ago about whether I like Zcash at this price.
[16:05] This is a pre-recorded podcast, so I guess it'll run on Wednesday, November the 12th.
[16:09] But very timely.
[16:11] It's sort of like... I again, there's the old crypto joke where like when your dentist and realtor friends start asking you about Ripple and Cardano, it's time to unwind your positions a little bit, you know?
[16:20] But it's the Zcash meta.
[16:22] I don't know, like, maybe that means there's room to run, maybe... maybe it's tops.
[16:26] But as they say, it's like catching a falling knife, right?
[16:28] Like, you know, trying to figure out the peak of the market.

**SPEAKER_01:**
[16:30] Okay, we've talked about kind of how Zcash works, and it uses ZK in these sort of very specific areas, and it's not programmable generally.
[16:37] Now, obviously, there's a lot of talk in the Ethereum world about ZK-EVMs.
[16:42] Do you guys have any thoughts on that and how those work?
[16:44] Because at what point do we get...
[16:46] Is it truly impossible to get full programmability or is that something that is just getting closer?

**SPEAKER_03:**
[16:51] From a market perspective, I think they're mostly... ZK-EVMs have been used for scaling as opposed to privacy.
[16:57] Even there, you tend to see some amount of specificity.
[17:00] Like I think I mentioned on a podcast before, I'm friend-acquaintances with the Lighter CEO, and Lighter uses...
[17:06] Lighter's like the L2 version of Hyperliquid, if you will, where they do perps and they do zero-knowledge matching off-chain, but you know it actually works and it gets written to Ethereum, which is pretty cool.
[17:16] And supposedly they're achieving really high throughputs this way.
[17:19] It's not necessarily privacy tech at all.
[17:21] I ran into some of the Aztec folks in Singapore and it seems trending general purpose, still on testnet, but not full EVM.
[17:29] It's like a restricted UTXO-type language of sorts, I believe.
[17:33] Um, so I think there's probably—not being nearly as expert as Jim, who I'll defer to in a second—not being an expert, I think it will be... there's no intrinsic reason you can't make it
[17:42] full EVM or full Rust or JavaScript or whatever, but probably there will be a tremendous amount of optimization that would have to happen to make that happen.
[17:50] So you probably see special purpose for a while.

**SPEAKER_00:**
[17:52] I saw that, and now I'm blanking on the name, the ZK tech that was happening under the Polygon
[17:57] banner with Jordi Baylina.
[18:01] And I can't remember the name of the project now.
[18:04] They posted within the last few months that they were real-time ZK proving mainnet now.
[18:09] But you know, it was with a battery of GPUs.
[18:11] It was not a thing that you would be doing yourself.
[18:13] But yeah, that full proving is, you know, is possible, but yeah, you have that optimization to be done.
[18:19] But I mean, I think that's where things are going to end up.
[18:21] That you've had this, um, sort of
[18:24] improvement where starting at Bitcoin it's like, "Well, how are we going to prove, you know, get to global consensus and and solve the double-spend problem?"
[18:31] "Well, it's by publishing all the details and then we're going to have, you know, redundant state machines running in parallel, right?"
[18:37] And that's the answer. We know that works.
[18:39] It was like what, you know, Satoshi did the big, ugly thing,
[18:43] but it worked and it made this stuff possible that had never been possible before.
[18:46] But it is, you know, it's an incredibly big, ugly, expensive way of doing that.
[18:50] And then I think just over time, it's like, okay, well...
[18:53] having things public was sort of a requirement for that consensus model, but that was never intentional.
[18:58] Like having them all as a public ledger, like that's not a positive feature.
[19:01] Now, if you look at the cypherpunk culture that many of these people were coming out of, yeah, it's private, unstoppable money.
[19:08] Like, yeah, no, it wouldn't be public.
[19:10] So I saw that within weeks
[19:12] of Bitcoin starting, Hal Finney said, you know, "Looking at ways of improving anonymity in Bitcoin."
[19:17] So that was January 2009.
[19:19] You know, that was a cypherpunk's obvious first reaction is, "Yeah, this is cool now.
[19:24] But yeah, we should have privacy as well."
[19:26] And I think we're sort of getting to that point of the tech has become good enough to solve that without broadcasting everything to everyone.

**SPEAKER_01:**
[19:32] Yeah, Jim, what do you think, like, you know, on the sort of general programmability ZK front?

**SPEAKER_02:**
[19:37] I wish I had more, you know, hands-on experience with general ZK.
[19:41] I see a lot of people very excited by it.
[19:44] And maybe in a way that makes me skeptical because it seems like a cool toy.
[19:48] But I am open to them working great.
[19:51] And so I don't want to make a strong, firm stance at the moment on them, but they would be great if they were.

**SPEAKER_01:**
[19:56] Yeah, it seems like the approach, to Kieran's point, is like find specific areas where you can create circuits and apply them and optimize for those and then expand that over time.
[20:04] You know, like it's really about kind of like,
[20:06] you know, nailing those initial use cases.

**SPEAKER_02:**
[20:08] And that's why I was drawn to that.
[20:09] Because if you really narrow it down to something really simple, then I think you can do it well.

**SPEAKER_03:**
[20:13] I've heard that people even maybe compile the specific circuits and then optimize.
[20:17] Like you kind of write them with the general tool.
[20:19] Some people do.
[20:20] I don't know.
[20:21] And then you kind of like, "Okay, I got the circuit for the specific thing, but then I got to make it like work."
[20:24] Yeah.

**SPEAKER_01:**
[20:25] I think compiling a circuit is still pretty very computational intensive, but it's way less...
[20:29] For most circuits, once a circuit is compiled, it's way less to do the proof.
[20:33] You got to continue to push that down, but I think the ratio is very large.
[20:36] Well, I think we are at time.
[20:38] You know, where can we find you, Jim?
[20:40] I'm going to start with you.
[20:41] Where can you find me?
[20:42] Yes.
[20:43] If you want to hear more and learn more about Jim, which I, you know, please speak up, ask him where can, where they find you.

**SPEAKER_02:**
[20:48] I do have a Twitter handle.
[20:50] What is my Twitter handle?
[20:51] I can't remember, but probably.

**SPEAKER_01:**
[20:53] I guess it's Jamshied, probably.

**SPEAKER_03:**
[20:55] I'm going to try to check.
[20:56] Hold on.
[20:57] Yeah.

**SPEAKER_01:**
[20:57] But whatever it is, you should post more often.

**SPEAKER_02:**
[21:00] I like wake up one day and remember that Twitter exists, and then I tweet a lot, and then I forget about it for a couple of weeks.

**SPEAKER_01:**
[21:06] Sorry, it's J-Hermos, like J-H-O-Y.

**SPEAKER_03:**
[21:08] I threw it in the chat.
[21:09] I don't know if we can all see that, the studio chat.

**SPEAKER_01:**
[21:11] Yeah.
[21:12] So, yes.
[21:12] You can find him at J-Hermos.
[21:14] Kieran, where can people find you?

**SPEAKER_03:**
[21:16] Jamshied Hermos.

**SPEAKER_01:**
[21:17] Oh, Jamshied Hermos.

**SPEAKER_03:**
[21:19] Yeah, I'm on X, K James Lubin.
[21:22] I'm also on Substack, trying to, you know, I have like a couple old Medium posts that I've linked from there.
[21:27] I'm getting a little bit into a Substack rhythm.
[21:29] It'll probably be infrequent, but at least of moderate to high quality.
[21:33] Also, K James Lubin, dot Substack.
[21:37] I think for now, maybe I'll change the URL, and link it to me in the show notes when we start assuming we do show notes.

**SPEAKER_01:**
[21:43] And you can find me on X at Vic Wong.
[21:46] Bob has posted why I explained before in my handle.
[21:49] You can also find us on Telegram at the Strong Mercato group.
[21:52] Just go to our website at strongmercato.com and that will point you to Telegram.
[21:57] And Bob, where can people find you and what can people expect next week?

**SPEAKER_03:**
[22:00] Don't close it out.
[22:01] Bob, you're the resident Zcash shill.
[22:03] One year from now, Zcash price or market cap or both?

**SPEAKER_00:**
[22:07] I think it will be in the top 10.
[22:08] Top 10?
[22:09] It's been very close.
[22:10] And the primary reason is privacy is a big need, and it's solved it, right?
[22:14] It's not some future promise.
[22:15] Like, it works right now.
[22:17] There's a mobile app.
[22:18] People are using it.
[22:19] You know, you've got like a 10-year, near 10-year history of...
[22:22] you know, top brainiacs working on this, lots of credibility.
[22:25] So you know, I think it's great.
[22:27] And then I'm looking forward to smart contracts with that kind of level as well.
[22:31] Just one more thing to mention, I couldn't remember Jordi's project: Zisk.
[22:36] So that's a spin-off group now from Polygon, led by Jordi Baylina, and they announced real-time proving of mainnet blocks.
[22:42] That was announced at FCC this year.
[22:44] So proving a block... in 7.5 to 12 seconds, so just under block time.
[22:49] However, it requires 24 very high-powered GPUs or 48 more consumer-spec.
[22:54] So you've got a rack.
[22:55] There you go.
[22:56] And Bob, with that prediction, where can we find you and can you give us a preview of what people can expect next week?

**SPEAKER_00:**
[23:01] Absolutely, yes.
[23:02] So I'm Bob Summerwill, Summer like the season, W-I-L-L.
[23:06] So on everything with that name.
[23:08] And yes, so next week, we will have an Early Days of Ethereum interview with Christoph Jentz, formerly of...
[23:14] fdev.
[23:15] So he was hired in September 2014 into that Berlin office, worked on testing, cross-client testing, and then later on Slock.it with their smart locks and the creation of The DAO, which is probably, you know, Ethereum's first killer app until the killing.
[23:29] Killing in many different ways, yes.

**SPEAKER_01:**
[23:31] Or you can say birthing, because ETC came out of that.
[23:33] Correct.
[23:34] Right.
[23:35] Okay.
[23:35] Well, that's time.
[23:36] Thank you very much for joining us.
[23:38] And we look forward to seeing you next week.
[23:40] Take care.

**SPEAKER_00:**
[23:41] Thanks, everybody.