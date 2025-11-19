**SPEAKER_00:**
[00:00] Okay. Welcome, everyone.
[00:01] We have a very special and very timely topic today: privacy on-chain and the rise of Zcash.
[00:09] And we sort of have a special guest today.
[00:10] So I'm Victor Wong.
[00:11] I am founder and chief product officer at BlockApps.
[00:15] I'll get to our normal guest, but today, we have Jim.
[00:17] Do you want to give us a quick intro?

**SPEAKER_01:**
[00:19] Yeah.
[00:19] I'm also—I've known Victor and Kieran for years.
[00:21] I'm one of the founders of BlockApps and CTO.

**SPEAKER_00:**
[00:26] And you're here in particular because I would call you a Zcash expert, having written your own Zcash client.

**SPEAKER_01:**
[00:33] Well, I think I'm more aspirational at this point in time.
[00:36] I mean, the way I learn about things is I try to—

**SPEAKER_02:**
[00:39] What's that?
[00:39] How many more expert people do you think there are on, say, Zcash in particular on the planet?

**SPEAKER_01:**
[00:44] No.
[00:44] The problem that I have is that I was sort of halfway in the learning process last year.
[00:49] So the way I learned about things is I try to, like, write a client for it.
[00:52] So I was doing that, but then we got pulled in different directions.
[00:55] I got to the point where I had sort of replicated the actual client that could connect.
[00:58] It would bring the data in.
[00:59] It would bring the proofs in.
[01:00] But just about when I was getting to the good parts, that's when we moved on to other things.
[01:04] Well, we're going to put the number—

**SPEAKER_00:**
[01:06] Answer my other question.
[01:07] Put the number at between, like, 10 and 100.
[01:09] Maybe 10.
[01:10] I would say there's definitely less than 20 people who have written their own Zcash clients, probably.
[01:14] Well, yeah.
[01:14] Yeah.
[01:15] There are probably some core contributors.

**SPEAKER_02:**
[01:17] I imagine there's more than a handful into Zcash.
[01:20] But, you know, when Jim says "non-expert," you know, it's like, there are—let's say yes.
[01:24] I'll expand the range.
[01:25] Five to 100 people who understand Zcash better on the planet.
[01:28] Big, big, big range there, but we're talking about pretty small numbers in absolute terms.
[01:32] So yeah. Yes. Exactly.
[01:33] I say—

**SPEAKER_00:**
[01:34] If Jim's not an expert, I don't know what expert even means.
[01:37] Anyways, Kieran, do you want to give a quick intro of yourself before we—

**SPEAKER_02:**
[01:40] Certainly. I'm our CEO.
[01:41] Been on these before.
[01:43] By the way, Vic, we're letting Jim off the hook calling him a special guest.
[01:46] He has to do this all the time now with our, you know, continued presence in the public press.
[01:49] So okay.

**SPEAKER_00:**
[01:50] Special now.
[01:50] Not special in the future.
[01:51] Special today.
[01:53] Today is special, but it's the first of many.
[01:54] Let's just say that.
[01:55] I was looking through the—the—

**SPEAKER_03:**
[01:56] —the prior videos.
[01:58] Jim has never appeared on one of our own Spaces.
[02:00] He's only been on early days of the year. Okay.

**SPEAKER_00:**
[02:02] Older drinks.
[02:02] Well, there you go.
[02:03] Oh, no.
[02:04] You found out.
[02:06] But it won't be special soon.
[02:07] Bob, by the way, since you've spoken up, can you give a quick intro to yourself?
[02:10] So, hi.
[02:11] I'm Bob.
[02:12] I'm head of ecosystem.

**SPEAKER_03:**
[02:13] And yeah, been doing a lot of a lot of Spaces.

**SPEAKER_00:**
[02:15] Yeah.
[02:15] So I think, you know, to level-set, because I think there's a lot of misunderstanding about what privacy is.
[02:20] How would you define blockchain privacy and why do you think it's important?

**SPEAKER_03:**
[02:23] Who's that question for?

**SPEAKER_00:**
[02:25] Could be for anyone.
[02:25] Whoever wants to go.
[02:27] Kieran, you want to kick us off?
[02:28] Okay.
[02:28] I'll take it.

**SPEAKER_02:**
[02:29] So, and for the—I assume that the viewer is pretty deep in the space, but I'll bring it down to a fairly low technical level.
[02:35] So blockchains are great.
[02:37] They let you move digitally scarce value from party to party.
[02:40] And the way that this is typically done is that you've got a big address, which is almost, but not quite, a public key, and you sort of sign a message that says, "I, Kiran"—but it's not Kiran because it's this address—"send, you know, 3 Bitcoin to Bob," and it doesn't say Bob.
[02:51] It's another address.
[02:53] You don't quite know who either of those parties are.
[02:55] However, you've got the address forever, and often it is the case that you can piece together what happened based on that address.
[03:01] Let's say you're on a centralized exchange, which has KYC'd.
[03:04] It knows how to associate you to maybe a withdrawal address.
[03:07] It may not know down the line, but if you start to get a bunch of data points, you can kind of piece together who sent what to whom, and you're actually in an extremely transparent scenario where everyone's financial transactions are visible to everyone.
[03:17] And it's not—while it's a cryptographic technology, it's not necessarily a private technology.
[03:22] And this has been a problem both in the consumer setting just because, you know, people don't like this.
[03:26] Satoshi makes a comment, I believe, in the white paper saying that, you know, obviously, to prevent the double-spend problem, which basically is just to ensure that assets can't be created or destroyed except by the agreed mechanism.
[03:37] Obviously, you need to know the whole history.
[03:39] And so he sees the problem as intrinsic, but some technologies have come out later that maybe call that into question, that we'll talk about.
[03:45] It's also an enterprise problem.
[03:47] So we can talk separately about our experience there.
[03:49] Sort of what the enterprises want is kind of the same as what the public blockchain people want, except with selective visibility.
[03:55] So they want to say you're doing, like, an on-chain stock trade, which is actually now starting to happen.
[04:00] You sort of want to know the other party has the stock.
[04:02] You don't necessarily want to know who the other party is, but you want to know that they acquired that stock legitimately.
[04:07] And then when you get it, you want to be able to pass it on legitimately in the same way.
[04:10] And then there's sometimes this extra requirement that, like, the regulator can see everything.
[04:14] You know?
[04:14] So you want sort of like an unlinkability of balance to person or company, but also this mass preservation property that I was talking about—you can't create or destroy assets.
[04:22] They have to be acquired legitimately and so on.
[04:25] So it's a perennial problem and closer to solved, you know, but we can go into that shortly.
[04:30] Yeah. Bob, did you want to add anything to that?

**SPEAKER_03:**
[04:33] Yeah.
[04:33] So, I mean, going back to those Bitcoin, you know, beginnings in the Bitcoin white paper, it just talks about severing identity from transactions.
[04:41] But really, that's just pseudonymous, you know, not anonymous.
[04:45] And I think a lot of people didn't understand that differentiation back in those early days, and it's like, "Oh, Bitcoin's private, untrackable, you know, digital money."
[04:52] But very rapidly, you have blockchain analytics coming in, looking for correlations and patterns, and it's like, yeah, that's—you're not getting a lot of security, you know, even if you're not reusing addresses, just normal things that people would do.
[05:01] There are lots of correlations and, you know, you can get unmasked that way.
[05:04] But yeah, Satoshi did talk a bit about zero-knowledge.
[05:07] I can't remember who raised it.
[05:08] Somebody raised it early, and he was like, "Yeah, you know, that would be interesting if we could do that."
[05:12] But it was just, like a lot of that cryptography just hadn't happened.
[05:16] You know?
[05:17] So Zcash started in 2016 and it was only around that kind of time or a little before that you started having, you know, these papers on STARK constructions and going through all these different kind of rounds.
[05:27] So, yeah, I mean, what that's meant is Bitcoin, and then Ethereum following that same path, you know, they are an immutable public ledger forever.
[05:33] Ethereum, even worse, because it's an account model.
[05:35] So you are reusing the addresses all the time. Right?
[05:38] And if your address is unmasked, you are forever doxed.
[05:41] That's happened to at least one of the Ethereum founders who moved hundreds of millions of dollars out of a known address of his, which is probably not desired.

**SPEAKER_00:**
[05:50] Well, and you know, you guys have been talking about Satoshi.
[05:53] But, Jim, I remember I think it was, like, earlier, like, 2014.
[05:56] Vitalik was talking—like, he was like, "A ZK-SNARK will fix all of this at some point in time."
[06:00] Do you remember that at all?

**SPEAKER_01:**
[06:02] Well, I mean, I think we went through a learning process about privacy, and we're understating this right now.
[06:08] Maybe it's because we put a lot of time and effort into some privacy solutions that technically worked but were a business failure, I think is fair to say.
[06:14] And so, you know, the audience can learn from our sort of failed mistakes in the past right now.
[06:18] But we sort of built—so we had heard years ago about ZK, but we sort of just—I don't know.
[06:23] At the time, we dove into it and said, like, "Oh, this looks overly complicated.
[06:26] You can get privacy through these other means."
[06:28] And we ended up building a system that allowed for a quick spin-up of private chains where everything was sort of in an encrypted tunnel, and you could have these chains completely secure.
[06:36] Nobody else would see what was happening there.
[06:38] But long story short, slow learning process, we found out that customers want everything, and to the point that it made it worthless.
[06:46] Like, we would go into enterprise, we would say, "Oh, you can set up these private channels with others."
[06:51] And they love that because they could sort of control that, and they could control who goes in there.
[06:55] But then once everything was going through these private channels, then they wanted to be able to transfer from private chain to private chain, and that's where everything started to fall apart.
[07:02] And getting things back onto the main chain became sort of this extra complicated system.
[07:07] And at the same time, customers wanted to have full flexibility in having, like, extensions to Solidity where you could just, like, name a chain and send some money from chain A to chain B.
[07:16] And really, the only way to make that stuff work is you have to go back to ZK.
[07:19] So ZK is overly complicated, but it is necessary.
[07:23] And so we started looking at that again, but I think the safe thing to do is start with a proven technology.
[07:27] And Zcash had been around for years, and nobody had stolen money.
[07:31] And this is just sort of like a subset of ZK, but it's kind of a cool thing.
[07:34] You can build what they call tumblers of money.
[07:36] You throw a bunch of money in, and then the money that you put into the tumbler is—you know how much went in, but the ownership is completely scrambled up.
[07:43] And at any time, you can go and transfer money from within the tumbler from one user to another, but only the users who did the transferring and got the money know what was there, but nobody else can see what's happening.
[07:52] So, again, you have these systems of multiple users with lots of money, but you don't know who owns what percentage of the money.

**SPEAKER_00:**
[08:00] Yeah.
[08:00] Actually, before we even go that far, can we talk just about, like, what is ZK and how does it work, and why is it an important part of the solution?
[08:06] I want to pull back for a second.

**SPEAKER_02:**
[08:08] I remember, I think there was an Ethereum meetup in New York.
[08:10] I'm not sure if either of you guys were there.
[08:12] I think I spoke at it, maybe.
[08:13] And there was also a Zcash, I think, presentation there.
[08:16] And it was, at that time, taking seven minutes to generate the ZK proofs.
[08:20] So yes.
[08:21] Yeah.
[08:21] You wanted to make a transaction.
[08:23] You'd, like, do this thing.
[08:24] It took seven minutes, and then the verification was kind of fast.
[08:27] Once you had it and you sent it to the network, things could go on, you know, but the usability was not there in those days.
[08:31] This is part of the reason we weren't, like, going to tell our enterprise customers, "Oh, yeah.
[08:34] Let's ZK everything."
[08:37] You know, even if we had it all integrated nicely, there's a lot of devil in the details.
[08:40] I know it was unbelievably—

**SPEAKER_01:**
[08:41] —slow for a while, and I think it's fixed.
[08:43] But yeah.
[08:44] I know.
[08:44] Well, it's complicated.
[08:45] I mean, this is what I was trying to say before.
[08:47] It's like, I have a sort of nuts-and-bolts experience of what's going on in Zcash.
[08:50] But the more complicated world of zero-knowledge, that's my aspirational part right now.
[08:55] I can sort of see pieces moving within there, but I would hesitate to speak more broadly on this.
[08:59] Except let's say that it is more complicated than any of the, like, for instance, Ethereum—

**SPEAKER_00:**
[09:02] —client implementation stuff that we were doing back in the day.
[09:04] Yeah. Yeah.
[09:05] Can you give a high-level summary of what zero-knowledge is?
[09:07] Like, I think very few people understand.

**SPEAKER_02:**
[09:09] I have a good layman example, I think, and Jim can correct me.
[09:12] Okay.
[09:12] So I did want to take a theoretical cryptography class, and the example they bring up is the CEO problem, so to speak.
[09:18] So we got two CEOs, and they're high-ego guys.
[09:21] You know?
[09:21] And they want to know—

**SPEAKER_00:**
[09:22] Does that stem from experience, Kieran?
[09:23] Or yeah.

**SPEAKER_02:**
[09:24] Yeah.
[09:24] Let's think about myself.
[09:26] They want to know who has the most between the two.
[09:28] But they don't want to know how much money.
[09:30] They merely want to know which one has more.
[09:32] And you would think that there wouldn't really be a way to create a scheme in which they could learn that information and nothing else, but there actually is.
[09:39] And again, this is almost ten years ago now, so I may be describing the example incorrectly.
[09:43] But yeah, that's like a case where you might want zero-knowledge.
[09:46] Similarly, like, you know, an ID check in a bar.
[09:48] You're leaking all your personal info when you hand the ID to the bouncer: your home address, your full name, your date of birth, you know, etcetera.
[09:54] So you may want to prove to the bar that you're 21 without handing any other info over, basically.
[09:59] I think this is the general setting that it ends up at.
[10:01] Jim, do you want to take that, run with it, correct it?
[10:03] Yeah.

**SPEAKER_01:**
[10:04] So this is—when you first look up zero-knowledge, there are lots of little examples like this.
[10:08] They're all pretty cool.
[10:09] But what's really happening in Zcash is that what you're trying to do is pass money from person A to person B.
[10:14] And person A wants to prove to person B that they have the money and that it was actually transferred, but without giving away the amount of money that person A has or without person A learning how much person B has.
[10:23] Just that, you know, the state before was that you had the amount and that the state after is that it was transferred over.
[10:28] And then also, no one else in the world can know this.
[10:30] So you're proving sort of the important parts, not others.
[10:33] Zero-knowledge can get pretty complicated too because when you start looking into it, there are a lot of one-off examples, like you're talking about, that you sort of see a solution to.
[10:41] But the problem comes about in trying to come up with a generic solution where you can almost just compile any amount of code into some ZK proof and then run that for anything.
[10:50] I don't remember because it's been about a year now, but in Zcash, there were multiple zero-knowledge proofs in there for various aspects.
[10:57] If I were—you know, I might be making up some of the details here, but I think there was one proof to show that you had more than such-and-such money before the transfer.
[11:04] I might have it slightly off, but there were multiple of these zero-knowledge algorithms in there.
[11:07] But put together, they allowed for the full sort of transfer of money within the tumbler.
[11:12] And each one sort of had been worked out independently of each other using a more generic system where they compiled certain algorithms in there.
[11:18] Does that make sense?
[11:19] So making it generic can get really complicated.

**SPEAKER_02:**
[11:21] Terminology for the listener that you've heard that I barely remember: So SNARKs and STARKs were a thing that Vitalik was talking about a lot and still does.
[11:28] So it's like Succinct, Non-interactive, ARgument of Knowledge... something.
[11:32] I can't remember.
[11:32] Like, but basically interactive proof.
[11:34] Yes.
[11:34] But what's the whole acronym?
[11:36] So there is a way, I think, to take an arbitrary computation and to prove that it has a certain result without revealing the intermediate states and so on.
[11:44] But it's not computationally feasible.
[11:45] Or it's just so slow that if you try to do it that way, it becomes very difficult.
[11:50] So I believe, just tying back to Jim's point, you could try to do this in generality.
[11:54] Like, the EVM. Like, I can verify—there are ZK-EVMs.
[11:57] Like, I can verify any computation that comes out of this thing.
[12:00] And I think the problem with them has been performance.
[12:02] And so the Zcash people, I guess, had to decompose every little step into specific ZK circuits. Right?
[12:08] Like or—Yeah. Yeah.
[12:09] So, yeah, it's very, very low-level programming thinking in the ZK world.
[12:12] Like, literally, there are circuits that you end up compiling and so on and so forth.

**SPEAKER_01:**
[12:15] Yeah, Zcash at the moment is onto it today.
[12:17] And sort of by identifying a certain set of algorithms and just focusing on them, they were able to solve this one tumbler problem without going any more in-depth than that.
[12:24] So this isn't like, in the dream world, you would take any, like, Ethereum contract and compile it somehow as a, you know, something zero-knowledge and then prove that you had run the full contract.
[12:33] That's something that, at the time, at least so far in the world as it is, I didn't want to get into it or have us get into it at the company.
[12:38] But just to have these tumblers in place, I think that solves a lot of—

**SPEAKER_03:**
[12:41] Yeah. Bob, were you saying something?
[12:43] Yeah.
[12:43] So Zcash is on to its fourth round of different cryptography.
[12:46] So I forget what they're called: Sapling, something else.
[12:49] We're on to Orchard now.
[12:50] But I mean, that's been now over the course of nearly a decade.
[12:53] You know, each time you've got another sort of two years' worth of leading-edge advancement.
[12:57] And yeah, like, talking about that performance thing.
[12:59] So it's something which I think has been a key piece in Zcash price appreciation recently has been the arrival of a functional mobile wallet.
[13:06] So that's called Zashi, which is made by the Electric Coin Company.
[13:10] But you're basically at the point where you can run that proof on your phone.
[13:13] So something which used to be laptop, seven minutes, is now phone, one second.
[13:17] So what you've seen, if you look at the size of these shielding pools, where these pools are effectively like, you know, all of these things are all mixed and hidden together. Right?
[13:24] The more that you've got in a pool, the more, you know, the more unlinkable you are.
[13:28] If you have—if you do something simple like ring signatures, where you just—whatever, I think Monero has got 16 transactions that get all joined together.
[13:37] So you can trace through that to a degree.
[13:39] But if you've got, you know, hundreds or thousands or millions of people in that same pool, you know, it's effectively completely anonymous at that point.
[13:47] But if you look at the stats of usage of these particular pools, are you seeing what proportion of the money supply has been shielded versus being transparent?
[13:54] I guess that's just another thing to say, right, is Bitcoin is transparent, you know, so same with Ethereum, but then they use the word "shielded" to talk about, you know, that you are within this anonymity set.
[14:04] So these earlier rounds, you know, you had a bit of use, but not a ton of use.
[14:07] But right now, I can't find the view, but it was something like about 4 or 5 million of the 21 million were within that shielding pool.
[14:14] So, you know, a significant chunk of it is shielded now, which was never the case in the past.
[14:18] You know?
[14:18] I remember on ETC at some point, we were looking at whether we were going to bring over the precompiles to do with some of the curves.
[14:24] You know?
[14:24] I don't know if you remember that happened in Ethereum at some point, but one of the curves, I think, went into the precompile.
[14:29] And we were talking about whether we were going to do that or not.
[14:31] And really, talking about gas limit as well, you know, like, how gas-expensive would operations be using these things even.
[14:37] And the stats at that time were, you know, it's like maybe 2% of transactions on Zcash were shielded, something like that.
[14:43] You know, it was basically not being used at all, you know, functionally pretty much identical to Bitcoin.
[14:48] But probably a lot of venues were going, "Yeah, I'm using Zcash.
[14:50] I'm private." It's like, "Yeah, you know, you are not at all."
[14:54] You're getting zero benefit at all.
[14:55] But yeah, that's really happening now.
[14:57] And I think it's just, you know, these rounds and rounds of years and years of research and then implementation of those and engineering effort, and it's like, "Hey, it works now."

**SPEAKER_00:**
[15:05] Well, I'm just curious from your standpoint, Jim, like, is it a technological advancement that has created this, or is it just simply that these tumblers have gotten big enough that they offer real privacy?
[15:13] Do you know what I mean?

**SPEAKER_01:**
[15:15] I mean, any of these things are technological advancements.
[15:17] But, I mean, you want to have the tumblers big enough so that you have some amount of anonymity within there.
[15:21] It's not like if it's a tumbler of one person, then it's not much of a tumbler.

**SPEAKER_02:**
[15:24] I need to interject.
[15:25] I have a crypto friend who was texting about thirty seconds ago about whether I like Zcash at this price.
[15:30] This is a prerecorded podcast.
[15:31] So, you know, well, I guess it'll run on Wednesday, November 12th.
[15:35] But very timely, you know, I think.
[15:37] It's sort of like—again, there's the old crypto joke where, like, when your dentist and realtor friends start asking you about Ripple and Cardano, it's time to unwind your positions a little bit.
[15:45] You know?
[15:45] But it's the Zcash meta. I don't know.
[15:47] Like, maybe that means there's room to run.
[15:49] Like, maybe it's tops.

**SPEAKER_00:**
[15:51] But well, as they say, it's like catching a falling knife.
[15:53] Right?
[15:53] Like, you know, yeah.
[15:55] Trying to figure out the peak of the market.
[15:57] Okay.
[15:57] Like, we've talked about kind of how Zcash works, and it uses ZK in these sort of very specific areas.
[16:02] And it's not, you know, programmable generally.
[16:04] Now, obviously, there's a lot of talk in the Ethereum world about ZK-EVMs.
[16:08] Do you guys have any thoughts on that and, like, you know, how those work?
[16:11] Because, you know, at what point do we get—like, is it truly impossible to get full programmability, or is that something that is just getting closer?

**SPEAKER_02:**
[16:17] From a market perspective, I think ZK-EVMs have been mostly used for scaling as opposed to privacy.
[16:22] Even there, you tend to see some amount of specificity.
[16:24] Like, I think I mentioned on a podcast before, I'm, you know, friends/acquaintances with the Lyra CEO, and Lyra uses—Lyra is like the L2 version of Hyperliquid, if you will, where they do perps and they do zero-knowledge matching off-chain, but you know it actually works and it gets written to Ethereum, which is pretty cool.
[16:39] And supposedly, they're achieving really high throughputs this way.
[16:41] It's not necessarily privacy tech at all.
[16:43] I ran into some of the Aztec folks in Singapore, and it seems trending general-purpose still on testnet, but not fully VM.
[16:50] It's like a restricted UTXO type language of sorts, I believe.
[16:53] So I think there's probably—not being nearly as expert as Jim, who I'll defer to in a second—not being an expert, I think there's no intrinsic reason you can't make it fully VM or full Rust or some, you know, JavaScript or whatever.
[17:05] But probably, there will be a tremendous amount of optimization that would have to happen to make that happen.
[17:09] So you'll probably see special-purpose for a while.

**SPEAKER_03:**
[17:11] I saw that—and now I'm blanking on the name.
[17:14] The ZK tech that was happening under the Polygon banner with—and I can't remember the name of the project now.
[17:19] They posted within the last few months that they were real-time ZK-proving mainnet now.
[17:23] But, you know, it was with a battery of GPUs.
[17:25] It was not a thing that you would be doing yourself.
[17:27] But yeah, that full proving is, you know, is possible.
[17:30] But yeah, you have that optimization to be done.
[17:32] But I mean, I think that's where things are going to end up.
[17:35] You've had this sort of improvement where starting at Bitcoin, it's like, "Well, how are we going to prove, you know, get to global consensus and solve the double-spend problem?"
[17:42] Well, it's by publishing all the details, and then we're going to have, you know, redundant state machines running in parallel. Right?
[17:48] And that's the answer we know that works.
[17:50] It was like, what's—you know, like, Satoshi did the big ugly thing, but it worked and it made this stuff possible that had never been possible before.
[17:57] But it is, you know, it's an incredibly big, ugly, expensive way of doing that.
[18:01] And then I think just over time, it's like, okay, well, having things public was sort of a requirement for that consensus model, but that was never intentional, like having them all as a public ledger.
[18:10] Like, that's not a positive feature.
[18:11] Now, if you look at the cypherpunk culture that many of these people were coming out of, yeah, it's private, unstoppable money.
[18:17] Yeah, no, it wouldn't be public.
[18:18] So I saw that, yeah.
[18:19] Within weeks of Bitcoin starting, Hal Finney said, you know, looking at ways of improving anonymity in Bitcoin.
[18:24] So that was January 2009.
[18:26] You know, that was a cypherpunk's obvious first reaction is, "Yeah, this is cool now.
[18:30] But, yeah, we should have privacy as well."
[18:32] And I think we're sort of getting to that point where the tech has become good enough to solve that without broadcasting everything to everyone.

**SPEAKER_00:**
[18:37] Yeah. Jim, what do you think?
[18:38] Like, you know, on the sort of general programmability ZK front.

**SPEAKER_01:**
[18:41] I wish I had more, you know, hands-on experience with general ZK.
[18:44] I see a lot of people very excited by it.
[18:46] And maybe in a way that makes me skeptical because it seems like a cool toy.
[18:49] But I am open to them working great.
[18:51] And so I don't want to make a strong firm stance at the moment on them, but they would be great if they work.

**SPEAKER_00:**
[18:56] Yeah.
[18:56] It seems like the approach, to Kieran's point, is like, find specific areas where you can, you know, create circuits and apply them and optimize for those and then expand that over time.
[19:04] You know?
[19:04] Like, it's really about kind of, you know, nailing those initial use cases then using the Zcash approach.

**SPEAKER_01:**
[19:08] And that's why I was drawn to that because, yeah, if you really narrow it down to something really simple, then I think you can do it well.

**SPEAKER_02:**
[19:12] I've heard that people even maybe compile the specific circuits and then optimize.
[19:15] Like, you kind of write them with the general tool.
[19:17] Some people do. I don't know.
[19:18] And then you kind of, like, "Okay, I got the circuit for the specific thing, but then I got to make it work." You know?
[19:22] Yeah.
[19:22] Maybe—

**SPEAKER_00:**
[19:23] I think compiling a circuit is still very, like, computationally intensive, but it's way less—for most circuits, once a circuit is compiled, it's way less to do the proof, which is—you know?
[19:30] And you've got to continue to push that down, but I think the ratio is very large.
[19:33] Okay.
[19:33] Well, I think we are out of time.
[19:35] You know, where can we find you, Jim?
[19:37] I'm going to start with you.
[19:38] Where can they find you?
[19:39] Yes.
[19:39] People want to hear more and learn more about Jim, which—I, you know, please speak up.
[19:42] Ask him where they can find you.

**SPEAKER_01:**
[19:44] I do have a Twitter handle.
[19:45] What is my Twitter handle?
[19:46] I can't remember.
[19:46] But—

**SPEAKER_00:**
[19:47] Probably @jormodel, I'm guessing.

**SPEAKER_02:**
[19:49] I'm going to try to check. Hold on. Yeah.

**SPEAKER_01:**
[19:51] But whatever it is, you should post more often on it.
[19:53] Okay.
[19:53] I Twitter in spurts.
[19:55] I, like, wake up one day and remember that Twitter exists, and then I tweet a lot, and then I forget about it for a couple of weeks.
[20:01] It's J H—

**SPEAKER_02:**
[20:02] O in the chat.
[20:03] I don't know if we can all see that, the studio chat.
[20:04] But yeah.

**SPEAKER_00:**
[20:05] So, yes, you can find him at @jhermas.
[20:07] Kieran, where can people find you?

**SPEAKER_02:**
[20:09] Hermas.

**SPEAKER_00:**
[20:09] Yeah.
[20:09] Oh, @jhermas.

**SPEAKER_02:**
[20:10] Yeah.
[20:10] I'm on X @KGLubin.
[20:12] I'm also on Substack.
[20:13] I'm trying to, you know—I'm like, a couple old Medium posts that I've linked from there.
[20:16] I'm getting a little bit into a Substack rhythm.
[20:18] It'll probably be infrequent, but at least of moderate to high quality.
[20:21] Also, kjameslubin.substack.com, I think, for now.
[20:24] Maybe I'll change the URL.
[20:25] Yeah. And link it in the show notes when we start—assuming we do show notes.

**SPEAKER_00:**
[20:29] And you can find me on X @vic4wang.
[20:32] Bob has posted why I explained before in my handle.
[20:34] You can also find us on Telegram at the Straum Mercado Group.
[20:37] Just go to our website at straummercado.com, and that will point you to Telegram.
[20:41] And, Bob, where can people find you, and what can people expect next week?
[20:44] Don't close it out.
[20:45] Bob, you're the resident Zcash shill.
[20:47] One year from now, Zcash—

**SPEAKER_02:**
[20:48] Price or market cap or both?

**SPEAKER_03:**
[20:50] I think it will be in the top 10.
[20:52] Top 10. It's been very close.
[20:54] And the primary reason is privacy is a big need, and it's solved it. Right?
[20:57] It's not some future promise. Like, it works right now.
[21:00] There's a mobile app. People are using it.
[21:02] You know?
[21:02] You've got, like, a near ten-year history of, you know, top brainiacs working on this.
[21:06] Lots of credibility. So, you know, I think it's great.
[21:09] And then I'm looking forward to smart contracts with that kind of level as well.
[21:13] Just one more thing to mention.
[21:14] I couldn't remember Jordi's project, Zeth.
[21:16] So that was—that's a spin-off group now from Polygon, led by Jordi Baylina, and they announced real-time proving of mainnet blocks that was announced at EthCC this year.
[21:24] So proving a block in seven and a half to twelve seconds, so just under block time.
[21:28] However, it requires 24 very high-powered GPUs or 48 more consumer spec.
[21:32] So you've got a rack.

**SPEAKER_00:**
[21:34] There you go.
[21:35] And Bob, with that prediction, where can we find you, and can you give us a preview of what people can expect next week?

**SPEAKER_03:**
[21:39] Absolutely.
[21:40] Yes.
[21:40] So I'm Bob Summerwill, summer like the season, w-i-l-l.
[21:44] So on everything with that name.
[21:46] And yes, so next week, we will have an "Early Days of Ethereum" interview with Christoph Jentzsch, formerly of the f.dev.
[21:53] So he was hired in September 2014 into that Berlin office, worked on testing, cross-client testing, and then later on, with their smart locks and the creation of The DAO, which is probably, you know, Ethereum's first killer app until it was killing—

**SPEAKER_00:**
[22:06] Killing in many different ways.
[22:08] Yes. We're doing that.
[22:09] Or you can say birthing, because ETC came out of that. Correct. Right.
[22:12] Okay.
[22:12] Well, that's time.
[22:14] Thank you very much for joining us, and we look forward to seeing you next week.
[22:16] Take care.
[22:17] Thanks, everybody.