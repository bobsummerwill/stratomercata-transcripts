**SPEAKER_00:**
[00:00] Okay, welcome, everyone.
[00:02] We have a very special and very timely topic today.
[00:04] Privacy on-chain and the rise of Zcash.
[00:07] And we sort of have a special guest today.
[00:09] So I'm Victor Wong.
[00:10] I am founder and chief product officer at BlockApps.
[00:13] I'll get to our normal guests, but today we have.
[00:15] Jim, do you want to give us a quick intro?

**SPEAKER_01:**
[00:17] Yeah.

**SPEAKER_02:**
[00:17] I'm also.
[00:18] I've known Victor and Kieran for years.
[00:20] I'm one of the founders of BlockApps and CTO.

**SPEAKER_00:**
[00:22] And you're here in particularly because I would call you a Zcash expert, having written your own Zcash client.

**SPEAKER_02:**
[00:28] Well, I think I'm more aspirational at this point in time.
[00:31] I mean, the way I learn about things is I try to.

**SPEAKER_01:**
[00:33] How many more expert people do you think there are on, say, Zcash in particular on the planet?

**SPEAKER_02:**
[00:38] No, the problem that I have is that I was sort of halfway in the learning process last year.
[00:42] So the way I learned about things is I try to, like, write.
[00:45] Write a client for it.
[00:47] So I was doing that, but then we got pulled in different directions.
[00:49] I got to the point where I had sort of replicated the actual client that could connect.
[00:53] It would bring the data in.
[00:54] It would bring the proofs in.
[00:56] But just about when I was getting to the good parts, that's when.
[00:59] When we moved on to other things.

**SPEAKER_00:**
[01:00] Well, I'm gonna put the number.

**SPEAKER_01:**
[01:01] Answer my own question, between like, 10 and 100, maybe 10.

**SPEAKER_00:**
[01:04] I would say there.
[01:05] There's definitely less than 20 people who have written their own Zcash clients.
[01:08] Probably.

**SPEAKER_01:**
[01:08] Well, yeah, there's probably some core contributors.
[01:10] I imagine there's more than a handful into Zcash.
[01:13] But, you know, when Jim says non-expert, he.
[01:15] You know, it's like there are.
[01:17] Let's say, yes, I'll expand the range 5 to 100 people who understand Zcash better on the planet.
[01:21] Big, big, big range there.
[01:23] But we're talking about pretty small numbers in absolute terms, so.

**SPEAKER_00:**
[01:26] Yeah, yes, exactly.
[01:27] I would say if Jim's not an expert, I don't know what even expert means.
[01:30] Anyways.
[01:31] Kieran, do you want to do a quick intro of yourself before?

**SPEAKER_01:**
[01:34] Certainly.
[01:35] I'm our CEO.
[01:36] Been on these before.
[01:37] By the way, Vic, you're letting Jim off the hook, calling him a special guest.
[01:40] He has to do this all the time now with our, you know, continued in the public press.
[01:44] So special in the future.

**SPEAKER_00:**
[01:45] Special today.
[01:46] Today is special, but it's the first of many.

**SPEAKER_03:**
[01:48] Let's just say that I was looking through the.
[01:49] The the prior videos Jim has never appeared on one of our own spaces.
[01:52] He's only been on early days of.

**SPEAKER_01:**
[01:54] Okay, there you go.

**SPEAKER_02:**
[01:55] Oh no, you found out but it.

**SPEAKER_00:**
[01:56] Won't be special soon.
[01:58] Bob, by the way, since you've spoken up, can you do give a quick intro to yourself?

**SPEAKER_03:**
[02:01] So hi, I'm.
[02:02] I'm Bob, I'm head of ecosystem and yeah been doing a lot of.
[02:05] A lot of spaces.

**SPEAKER_00:**
[02:06] Yeah so I, I think you know to level set because I think there's a lot of misunderstanding about what privacy is.

**SPEAKER_01:**
[02:11] What.

**SPEAKER_00:**
[02:12] How would you define blockchain privacy and why do you think it's important?

**SPEAKER_03:**
[02:15] Who's that a question for?

**SPEAKER_00:**
[02:16] Could be for anyone.
[02:17] Whoever wants to go Kieran, you want.

**SPEAKER_01:**
[02:18] to kick us off so and for the.
[02:20] I assume that the viewer is pretty deep in the space but I'll bring it down to a fairly low technical level.
[02:24] So blockchains are great.
[02:26] They let you move digitally scarce value from party to party.
[02:29] And the way that this is typically done is that you've got a big address which is almost but not quite a public key and you sort of sign a message that says I, Kieran, but it's not Kieran because it's this address.
[02:37] Send three Bitcoin to Bob and it doesn't say Bob.
[02:39] It's another address you don't quite know either of those parties are.
[02:42] However you've got the address forever.
[02:44] And often it is the case that you can piece together what happened based on that address.
[02:48] So say you're on a centralized exchange which has KYC'd.
[02:51] It knows how to associate you to maybe a withdrawal address.
[02:54] It may not know down the line but if you start to get a bunch of data points you can kind of piece together who sent what to whom and you're actually in an extremely transparent scenario where everyone's financial transactions are visible to everyone and it's not.
[03:04] While it's a cryptographic technology, it's not necessarily a private technology.
[03:08] This has been a problem both in the consumer setting just for.
[03:10] People don't like this.
[03:11] Satoshi makes a comment, I believe in the white paper saying that obviously to prevent the double-spend problem which basically is just that to ensure that Bitcoin can't be created or destroyed except by the agreed mechanism.
[03:22] Obviously you need to know the whole history and so he sees the problem as intrinsic.
[03:26] But some technologies come out later that maybe calls that into question that we'll talk about.
[03:30] It's also an enterprise problem so we can talk separately about our experience there.
[03:33] Sort of what the enterprises want is kind of the same as what the public blockchain people want, except with selective visibility.
[03:39] So they want to say you're doing like a.
[03:41] on-chain stock trade, which is actually now starting to happen.
[03:44] You sort of want to know the other party has the stock.
[03:46] You don't necessarily want to know who the other party is, but you want to know that they acquired that stock legitimately.
[03:51] And then when you get it, you want to be able to pass it on legitimately in the same way.
[03:54] And then there's sometimes this extra requirement that like, the regulator can see everything, you know, so you, you want sort of like an unlinkability of balance to person or company, but also this mass preservation property that I was talking about can't create or destroy assets.
[04:06] They have to be acquired legitimately and so on.
[04:08] So it's a perennial problem and closer to solved and, you know, but we can go into that shortly.

**SPEAKER_00:**
[04:13] Yeah, Bob, did you want to add anything to that?

**SPEAKER_03:**
[04:14] Yeah, yes.
[04:15] I mean, going back to those Bitcoin, you know, beginnings in the Bitcoin white paper, you know, it, it just talks about severing identity from transactions, but, but really that's just pseudonymous, you know, not, not anonymous.
[04:26] And I think a lot of people didn't understand that differentiation back in those early days.
[04:29] And it's like, oh, Bitcoin's private, untrackable, you know, digital money.
[04:33] But, you know, very rapidly you have blockchain analytics coming in, you know, looking for correlations and patterns.
[04:38] And it's like, yeah, that's.
[04:39] You're not getting a lot of security, you know, even if you're not reusing addresses, just, just sort of normal things that people would do.
[04:45] There's, there's lots of correlations and you know, you can get unmasked that way.
[04:48] But yeah, Satoshi did talk a bit about zero-knowledge.
[04:51] I can't remember who raised it.
[04:52] Somebody raised it early and, and he was like, yeah, you know, that would be interesting if we could do that.
[04:56] But, but it was just like a lot of that cryptography, you know, just didn't, hadn't happened, you know, so Zcash started in 2016, and it was only around that kind of time or a little before that you started having, you know, these, these papers on, on SNARK constructions and going through all these different kind of rounds.
[05:10] So, yeah, I mean, what that's meant is Bitcoin and then Ethereum following that same path.
[05:15] You know, they are an immutable public ledger forever.
[05:17] Ethereum.
[05:18] Even worse because it's an account model.
[05:20] So you're, you are reusing the addresses all the time, right?
[05:23] And if your address is unmasked, you are forever doxxed.
[05:26] That's happened to at least one of the Ethereum founders who moved hundreds of millions of dollars and out of a known address of his, which probably not desired.

**SPEAKER_00:**
[05:32] And you guys have been talking about Satoshi, but Jim, I remember, I think it's like early at like 2014, Vitalik was talking like, he was like, ZK-SNARK will fix all of this at some point in time.
[05:43] Do you remember that?

**SPEAKER_02:**
[05:43] Well, I mean, like, I think we went through a learning process about privacy.
[05:47] And that's sort of like we're understating this right now.
[05:49] Maybe it's because we put a lot of time and effort into some privacy solutions that technically worked but were a business failure, I think is fair to say.
[05:56] And so the audience can learn from our failed mistakes in the past right now.
[05:59] But we sort of built.
[06:01] So we had heard years ago about ZK, but we sort of just, I don't know, at the time, looked into it and said like, oh, this looks like overly complicated.
[06:08] You can get privacy through these other means.
[06:10] And we ended up building a system that, that allowed for sort of like quick spin up of, of private chains that everything was sort of like in a, an encrypted tunnel.
[06:18] And you could, you could have like these chains completely secure.
[06:20] Nobody else would see what was happening there.
[06:22] But, but long story short, you know, slow learning process, we, we found out that customers want everything.
[06:27] And to the point that it made it worthless, we would go into enterprise.
[06:30] We would say, oh, you can set up these private channels with others.
[06:33] And they love that because they could sort of control that and they could control who goes in there.
[06:36] But then once everything was going through these private channels, then they wanted to be able to transfer from private chain to private chain.
[06:42] And that's where everything started to fall apart.
[06:44] Getting things back onto the main chain became sort of this extra complicated system.
[06:48] And at the same time, customers wanted to have full flexibility in having extensions to Solidity where you could just name a chain and send some money from chain A to chain B.
[06:56] And really the only way to make that stuff work is you have to go back to ZK.
[06:59] So ZK is overly complicated, but it is necessary.
[07:03] And so we started looking at that again.
[07:05] But I think the safe thing to do is start with a proven technology.
[07:08] And Zcash had been around for years and nobody had stolen money.
[07:11] And this is just sort of like a subset of ZK, but it's kind of a cool thing.
[07:14] You can build what they call tumblers of money, throw a bunch of money in and then the money that you put into the tumbler is, you know how much went in but, but the ownership is completely scrambled up and at any time you can go and transfer money from within the tumbler from one user to another, but only the users who did the transferring and got the money know what was there, but nobody else can see what's happening.
[07:29] So again like you have these systems of multiple users with lots of money, but you don't know who owns a percentage of the money.

**SPEAKER_00:**
[07:35] Yeah.
[07:35] Actually before we even go that far, can we talk just like what is ZK and how does it work and why is it an important part of the solution?

**SPEAKER_01:**
[07:42] I want to pull back for also a second.
[07:44] I remember, I think there was an Ethereum meetup in New York.
[07:46] I'm not sure if either of you guys were there.
[07:48] I think I spoke at it maybe and there was also a Zcash I think presentation there.
[07:52] And it was at that time taking seven minutes to generate the ZK proofs.
[07:56] So you wanted to make a transaction you'd like, did this thing, it took seven minutes and then the verification was kind of fast.
[08:01] Once you had it and you sent it to the network, things could go on.
[08:03] But the usability was not there in those days.
[08:05] This is part of the reason we weren't gonna tell our enterprise customers like oh yeah, let's, let's ZK everything.
[08:11] You know, even if we had it all integrated nicely, there's a lot of devil in the details and it was unbelievably slow for a while and I think it's fixed.

**SPEAKER_00:**
[08:18] But yeah, well, it's complicated.

**SPEAKER_01:**
[08:19] I mean this is what I was.

**SPEAKER_02:**
[08:20] trying to say before is like I have like sort of nuts and bolts experience of what's going on in Zcash.
[08:25] But the more complicated world of zero-knowledge, that's my aspirational part right now.
[08:29] I can sort of see pieces moving within there but, but would hesitate to speak more broadly on this except let's say that, that, that it is more complicated than any of the like for instance, Ethereum client implementation stuff that we were doing back in the day.

**SPEAKER_00:**
[08:42] Yeah, yeah.
[08:42] It can get pretty high level summary of what zero-knowledge is like.
[08:45] I think very few people understand.

**SPEAKER_01:**
[08:46] I, I, I have a good layman example.
[08:49] Okay.
[08:49] I think and Jim can correct me.
[08:51] So I, I did want to take a theoretical cryptography class and the example they bring up is the CEO problem, so to speak.
[08:56] So you've got two CEOs and they're high ego guys, you know, and they want to know do you stand up.

**SPEAKER_00:**
[09:00] From experience, Kieran, or.

**SPEAKER_01:**
[09:02] Yeah, I'm not speaking about myself.
[09:03] They want to know who has the most between the two, but they don't want to know how much money, they merely want to know which one has more.
[09:09] And you would think that there wouldn't really be a way to create a scheme in which they could learn that information and nothing else.
[09:14] But there actually is.
[09:16] Again, this is almost 10 years ago now, so I may be describing the example incorrectly, but yeah, that's like a case where you might want zero-knowledge.
[09:22] Similarly, like an ID check at a bar, you're leaking all your personal info when you hand the ID to the bouncer, to your home address, your full name, your date of birth, etc.
[09:29] So you may want to prove to the bar that you're over 21 without handing any other info over.
[09:34] Basically I think this is the general setting that it ends up at.
[09:36] Jim.
[09:36] Do I.
[09:37] You want to take that and run with it?
[09:38] Correct it?

**SPEAKER_00:**
[09:39] Yeah.

**SPEAKER_02:**
[09:39] So this is when you first look up zero-knowledge.
[09:42] There are lots of little examples like this that are all pretty cool.
[09:45] And what's really happening in Zcash is that what you're trying to do is pass money from person A to person B.
[09:50] And person A wants to prove to person B that they have the money and that it was actually transferred, but without giving away the amount of money that person A has.
[09:58] Or without person A learning how much that person B has.
[10:01] Just that you know, that the state before was that you had the amount and that the state after is that it was transferred over.
[10:06] And then also no one else in the world can know this.
[10:08] So you're proving sort of the important parts but not others.
[10:11] But zero-knowledge could get pretty complicated too because when you start looking into it, there are a lot of one off examples like you're talking about that you can sort of see a solution to.
[10:18] But the problem comes about in trying to come up with sort of a generic solution where you can almost just compile any amount of code into some ZK proof and then run that for anything.
[10:28] I don't remember because it's been about a year now, but, but in Zcash there were multiple, multiple zero-knowledge proofs in there for various aspects.
[10:35] If I, you know, I might be making up some of the details here, but I think there was like one proof was like to show that you had more than such and such money before the transfer.
[10:43] I might have it slightly off, but there were multiple of these zero-knowledge algorithms in there.
[10:47] But put together they allowed for the, for the full sort of transfer of money within the tumbler.
[10:51] And each one sort of had been worked out independently of each other using a more generic system where they compiled certain algorithms in there, let me add.
[10:58] So making it generic can get really.

**SPEAKER_01:**
[10:59] Complicated terminology for the listener that you heard that I barely remember.
[11:03] So SNARKs and STARKs were a thing that Vitalik was talking about a lot and still does.
[11:07] So it's like succinct, non-interactive arbitrary something computation.
[11:11] I can't remember.

**SPEAKER_03:**
[11:12] Like but basically interactive proof.

**SPEAKER_01:**
[11:14] Yes, but what's the whole acronym?
[11:15] But so there is a way I think to take an arbitrary computation and to prove that it has a certain result without revealing like the intermediate states and so on.
[11:23] But it's not computationally feasible.
[11:25] Like or it's just so slow that if you try to do it that way it becomes very difficult.
[11:29] So I believe just, just tying back to Jim's point, like you could try to do this in a generality.
[11:34] Like I can verify like the EVM.
[11:36] Like I can verify there are these ZK-EVMs like I verify any computation that comes out of this thing.
[11:41] And I think the problem with them has been performance.
[11:43] And so the Zcash people, I guess had to decompose every little step into specific circuits.
[11:48] Right.
[11:48] Like or.
[11:49] Yeah, it's very, very low level programming thinking in the ZK world.
[11:53] Like literally they're circuits that you end up compiling and so on and so forth.

**SPEAKER_03:**
[11:57] So yeah, Zcash at the moment is onto it.

**SPEAKER_01:**
[11:59] Yeah.

**SPEAKER_02:**
[11:59] And sort of by identifying a certain set of algorithms and just focusing on them, they were able to sort of solve this one Tumblr problem without going any more in depth than that.
[12:07] So this isn't like in the dream world.
[12:09] You would take any Ethereum contract and compile it somehow as a something zero-knowledge and then prove that, that you had run the, the full contract.
[12:16] That's something that at the time, at least so far in the world as it is, I, I didn't want to get into it or have us get into it as a company, but just to have these tumblers in place, I think that solves a lot of.

**SPEAKER_00:**
[12:25] Yeah, Bob, you were saying something.

**SPEAKER_03:**
[12:26] Yeah.
[12:26] So Zcash is onto its fourth round of different cryptography.
[12:30] So I forget what they're called sapling something else or onto Orchard now.
[12:34] But I mean that's been now over the course of nearly a decade.
[12:36] You know, each time you've got another sort of two years worth of leading edge advancement and yeah like talking about that performance thing.
[12:43] So something which I think has been a key piece in Zcash price appreciation recently has been the arrival of a functional mobile wallet.
[12:50] So that's called Zashi, which is made by the Electric Coin Company.
[12:53] But you're basically at the point where you can run that proof on your phone.
[12:56] So something which used to be laptop 7 minutes is now phone second.
[13:00] So what you've seen if you look at the size of these shielding pools, where these pools are effectively like, you know, all of these things are all, you know, mixed and hidden together.
[13:08] Right.
[13:08] The, the more that you've got in a pool, the more you know, the more unlinkable you are if you have a, you know, if you do something simple like ring signatures where you just whatever.
[13:16] I think Monero's got 16 transactions that get all joined together.
[13:19] So you can trace through that to a degree.
[13:21] But if you've got hundreds or thousands or millions of people in that same pool, it's effectively completely anonymous at that point.
[13:27] But if you look at the stats of usage of these particular pools, are you seeing what proportion of the money supply has been shielded versus being transparent?
[13:34] I guess that's another thing to say, right?
[13:36] Is, is Bitcoin is transparent, you know, so same, same with Ethereum.
[13:39] But then they, they, they use the world word shielded to talk about, you know, that you are within this anonymity set.
[13:45] So these earlier rounds, you know, you had a bit of use but not a ton of use.
[13:48] But right now I can't find the view.
[13:50] But it, but it was something like about 4 or 5 million of the 21 million were within that shielding pool.
[13:55] So you know, a significant chunk of it is shielded now which was never the case in the past.
[13:59] You know I remember on ETC at some point we were looking at whether we were going to bring over the precompiles to do with some of the curves.
[14:05] I don't know if you remember that happened in Ethereum at some point.
[14:07] One of the BLAKE curves I think went into the precompile and we were talking about whether we were going to do that or not.
[14:12] And really talking about gas limit as well.
[14:14] How gas expensive would operations be using these things even?
[14:17] And the stats at that time were it's like maybe 2% of transactions on Zcash were shielded, something like that.
[14:22] It's basically not being used at all functionally.
[14:25] Pretty much identical to Bitcoin but probably a lot of end users going, yeah, I'm using Zcash, I'm private.
[14:30] It's like, yeah, you're not at all.
[14:31] You are getting zero benefit at all.
[14:33] But yeah, that's really happening now.
[14:35] And I think it's just these rounds and rounds and years and years of research and then implementation of those.
[14:40] An engineering effort and it's like, hey, it works now.

**SPEAKER_00:**
[14:42] Well, from your standpoint, Jim, like, is it a technological advancement that Zcash has created or is it just simply that these tumblers have gotten big enough that they offer real privacy?
[14:52] Do you know what I mean?

**SPEAKER_02:**
[14:53] It's, I mean any of these things are technological advancements, but I mean, you want to have the tumblers big enough so that, that you have some amount of anonymity within there.
[15:00] If it's a tumbler of one person, then it's not much of a tumbler.

**SPEAKER_01:**
[15:03] I need to interject.
[15:04] I have a crypto friend who was, was texting about 30 seconds ago about whether I like Zcash at this price.
[15:09] This is a pre recorded podcast.
[15:11] So, you know, well, I guess it'll run on Wednesday, November 12, but very timely.
[15:15] You know, I think it's sort of like again, this is the old crypto joke where like when your dentist and realtor friends start asking you about Ripple and Cardano, time to unwind your positions a little bit.
[15:25] You know, it's the Zcash meta.
[15:27] I don't know, like, maybe that means there's room to run, maybe, maybe it's tops.

**SPEAKER_00:**
[15:30] But, well, as they say, it's like catching a falling knife, right?
[15:33] Like, you know, trying to figure out the, the peak of the market.
[15:35] I, I, okay, like we've talked about kind of how Zcash works and it uses ZK in these sort of very specific areas and it's not, you know, programmable generally.
[15:44] Now obviously there's a lot of talk in the Ethereum world about ZK-EVMs.
[15:48] Do you guys have any thoughts on that?
[15:49] And like, you know how those work?
[15:51] Because, you know, at what point do we get like, is it truly impossible to get full programmability?
[15:56] Or do you know, is that something.

**SPEAKER_01:**
[15:57] that is just getting closer from a market perspective?
[16:00] I think they're mostly ZK-EVMs have been used for scaling as opposed to privacy.
[16:04] Even there you tend to see some amount of specificity.
[16:06] Like I think I mentioned on a podcast before, I'm, you know, friend acquaintances with the Lighter CEO and Lighter uses.
[16:12] Lighter is like the L2 version of Hyperliquid, if you will, or where they do perps and they do zero-knowledge matching off chain but you know, it actually works and it gets written to Ethereum which is pretty cool and supposedly they're achieving really high throughputs this way.
[16:24] It's not necessarily privacy tech at all.
[16:26] I ran into some of the Aztec folks in Singapore that seems trending.
[16:30] General purpose still on testnet but not full EVM.
[16:33] It's like a restricted UTXO type language of sorts I believe.
[16:36] I think there's probably not being nearly as expert as Jim, who I'll defer to in a second not being an expert.
[16:42] I think it will be.
[16:43] There's no intrinsic reason you can't make it full EVM or full Rust or JavaScript or whatever.
[16:47] But probably there will be a tremendous amount of optimization that would have to happen to make that happen.
[16:51] So you probably see special purpose for a while.

**SPEAKER_03:**
[16:53] I saw that and now I'm blanking on the name.
[16:55] The ZK tech that was happening under the Polygon banner with Jordi Baylina and I can't remember the name of the project now they posted within the last few months that they were real time ZK proving mainnet now but you know, it was with a battery of GPUs.
[17:06] It was not a thing that you would be doing yourself.
[17:08] But yeah, that full proving is, you know, is possible, possible.
[17:12] But yeah, you, you, you have that optimization to, to be done.
[17:14] But I mean I think, I think that's where things are going to end up that you've had this sort of improvement where starting at Bitcoin, it's like well how are we going to prove, you know, get to global consensus and, and solve the double-spend problem?
[17:24] Well it, it's by publishing all of the details and then we're going to have redundant state machines running in parallel.
[17:29] Right.
[17:29] And that's the answer.
[17:30] We know that works.
[17:31] It was like what Satoshi did the big ugly thing but it worked and it made this stuff possible that had never been possible before, but it is, you know, it's an incredibly big, ugly, expensive way of doing that.
[17:41] And then I think just over time it's like okay, well having things public was sort of a requirement for that consensus model.
[17:47] But that was never intentional.
[17:48] Like having them all as a public ledger like that, that's not a positive feature.
[17:51] Now if you look at the cypherpunk culture that many of these people were coming out of, yeah, it's, it's private, unstoppable money.
[17:57] Like yeah, no, it wouldn't be public.
[17:59] So I saw that, yeah.
[18:00] Within weeks of bitcoin starting, Hal Finney said, you know, looking at ways of improving anonymity in Bitcoin.
[18:05] So that was January 2009.
[18:07] You know, that was a cypherpunk's obvious first reaction is, yeah, this is cool now, but yeah, we should have privacy as well.
[18:13] And I think we're sort of getting to that point of the tech has become good enough to, to solve that without broadcasting everything to everyone.

**SPEAKER_00:**
[18:19] Yeah.
[18:19] Jim, what, what do you think, like, you know, on the sort of general programmability ZK front?

**SPEAKER_02:**
[18:24] I wish I had more, you know, hands on experience with general ZK.
[18:27] I see a lot of people very excited by it and maybe in a way that makes me skeptical because it seems like a cool toy, but I am open to them working great.
[18:35] And so I don't want to make a strong, firm stance at the moment on them, but they would be great if they work.

**SPEAKER_00:**
[18:40] Yeah.
[18:40] It seems like the approach to Kieran's point is like find specific areas where you can create circuits and apply them and optimize for those and then expand that over time.
[18:48] It's really about nailing those initial use cases.

**SPEAKER_02:**
[18:50] And that's why I was drawn to that, because if you really narrow it down to something really simple, then I think you can do it.
[18:55] Well.

**SPEAKER_01:**
[18:55] I've heard that people even maybe compile the specific circuits and then optimize like you kind of write them with the general tool.
[19:00] Some people do, I don't know.
[19:02] And then you kind of like, like, okay, I got the circuit for the specific thing, but then I got to make it like work, you know.

**SPEAKER_00:**
[19:07] Yeah, I think compiling a circuit is still pretty very like computational intensive.
[19:11] But it's way more, but it's way less for most circuits once the circuit is compiled.
[19:15] It's way less to do the proof, which is, you know, and you got to continue to push that down, but I think the ratio is very large.
[19:20] Okay, well, I think we are at time, you know, where can we find you?
[19:23] Jim, I'm going to start with you.

**SPEAKER_02:**
[19:25] Where can you find me?

**SPEAKER_00:**
[19:26] Yes, people, I hear more and learn more about Jim, which I, you know, please speak up.
[19:29] Ask Jim, where can, where they find you?

**SPEAKER_02:**
[19:31] I do have a Twitter handle.
[19:33] What is my Twitter handle?
[19:34] I can't remember, but probably J.
[19:36] Hermuz.

**SPEAKER_00:**
[19:37] I guess it's jam.
[19:38] She probably try to check.

**SPEAKER_01:**
[19:39] Hold on.

**SPEAKER_02:**
[19:40] Yeah.

**SPEAKER_00:**
[19:40] But whatever it is, you should post more often.
[19:42] Okay.

**SPEAKER_02:**
[19:42] I, I Twitter.
[19:44] I like wake up one day and remember that Twitter exists.
[19:46] And then I Twitter, I tweet a lot and then.
[19:48] Then I forget about it for a couple.

**SPEAKER_00:**
[19:50] Sorry, it's J for months like J.

**SPEAKER_01:**
[19:51] H O in the chat.
[19:52] I don't know if we can all see that the studio chat.

**SPEAKER_00:**
[19:54] But yeah, so.
[19:55] So yes, you can find them at J Hermuz.

**SPEAKER_01:**
[19:57] Kieran, where can people find Hermes?

**SPEAKER_00:**
[19:59] Oh, Jamsheed Hormoz.

**SPEAKER_01:**
[20:01] Yeah, I'm on X Rubin.
[20:03] I'm also on substack trying to, you know, I have a couple old medium posts that I've linked from there.
[20:06] I'm getting a little bit into a substack rhythm.
[20:08] It'll probably be infrequent but at least of moderate to high quality.
[20:12] Also kjameslubin Substack I think for now maybe I'll change the URL and link it in the show notes when we start.
[20:17] Assuming we do show notes and you.

**SPEAKER_00:**
[20:18] can find me on xicforwang.
[20:20] Bob has posted why I explained before in my handle.
[20:23] You can also find us on Telegram at the Strom Mercado Group.
[20:26] Just go to our website@straumercada.com and that will point you to Telegram.
[20:30] And Bob, where can people find you and what can people expect next week?

**SPEAKER_01:**
[20:33] Don't close it out, Bob.
[20:34] You're the resident Zcash shill.
[20:36] One year from now, Zcash price or market cap or both?

**SPEAKER_03:**
[20:40] I think it will be in the top 10.

**SPEAKER_01:**
[20:42] Top 10.

**SPEAKER_03:**
[20:42] It's been very close and the primary reason is privacy is a big need and it solved it, right?
[20:48] It's not some future promise like it works.
[20:50] Right now there's a mobile app, people are using it.
[20:52] You know, you've got like a 10 year, near 10 year history of, you know, top brainiacs working on this.
[20:57] Lots of credibility.
[20:58] So you know, I think it's great and then I'm looking forward to smart contracts with that kind of level as well.
[21:03] Just one more thing to mention.
[21:04] I couldn't remember Jordi's project Zisk.
[21:06] So that was.
[21:07] That's a spinoff group now from Polygon led by Jordi Baylina and they announced real time proving of mainnet blocks that was announced at EthCC this year.
[21:14] So proving a block in 7 1/2 to 12 seconds.
[21:17] So just under block time.
[21:18] However, it requires 24 very high powered GPUs or 48 more consumer spec.
[21:23] So you've got a rack.

**SPEAKER_00:**
[21:24] There we go.
[21:24] And Bob, with that prediction, where can we find you and can you give us a preview of what people can expect next week?

**SPEAKER_03:**
[21:30] Absolutely, yes.
[21:31] So I'm Bob Summerwill.
[21:32] Summer like the season.
[21:33] W I L L so on everything with that name.
[21:36] And yes.
[21:37] So next week we will have an early days of Ethereum interview with Christoph Jentzsch, formerly of.
[21:42] of the Ethereum Foundation, so was hired in September 2014 into that Berlin office, worked on testing, cross client testing and then later on Slock.it with their smart locks and the creation of the DAO, which was probably, you know, Ethereum's first killer app.
[21:56] Until killing.

**SPEAKER_00:**
[21:57] Killing in many different ways.
[21:58] Yes, by doing that.
[21:59] Or you can say birthing because ETC came out of that.

**SPEAKER_03:**
[22:02] Correct.
[22:02] Right.

**SPEAKER_00:**
[22:03] Okay.
[22:03] Well, that's time.
[22:04] Thank you very much for joining us and we look forward to seeing you next week.
[22:07] Take care.

**SPEAKER_01:**
[22:08] Thanks, everybody.