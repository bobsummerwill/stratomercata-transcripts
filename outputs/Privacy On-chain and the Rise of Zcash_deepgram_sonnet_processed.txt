# Corrected Transcript

**SPEAKER_00:**
[00:00] Okay, welcome everyone. We have a very special and very timely topic today: privacy on-chain and the rise of Zcash. And we sort of have a special guest today. So I'm Victor Wong. I am founder and chief product officer at Block Apps.

[00:20] I'll get to our normal guest, but today we have Jim. Do you want to give us a quick intro?

**SPEAKER_01:**
[00:27] Yeah, I'm also—I've known Victor and Kiran for years. I'm one of the founders of Block Apps and CTO.

**SPEAKER_00:**
[00:36] And you're here in particular because I would call you a Zcash expert, having written your own Zcash client.

**SPEAKER_01:**
[00:43] Well, I think I'm more aspirational at this point in time. I mean, the way I learn about things is I try to—

**SPEAKER_02:**
[00:51] What's that? More expert people do you think there are on, say, Zcash in particular on the planet?

**SPEAKER_01:**
[00:58] No, the problem that I have is that I was sort of halfway in the learning process last year. So the way I learned about things is I try to write a client for it. So I was doing that, but then we got pulled in different directions.

[01:13] I got to the point where I had sort of replicated the actual client that could connect. It would bring the data in. It would bring the proofs in. But just about when I was getting to the good parts, that's when we moved on to other things.

**SPEAKER_00:**
[01:28] Well, we're going to put the number—answer my other question. Put the number at between like 10 and 100.

[01:35] Maybe 10. I would say there's definitely less than 20 people who have written their own Zcash clients, probably.

**SPEAKER_01:**
[01:42] Well, yeah. Yeah, there's probably some core contributors.

**SPEAKER_02:**
[01:45] I imagine there's more than a handful into Zcash. But, you know, when Jim says non-expert, he—you know, it's like there are—let's say yes, I'll expand the range: five to 100 people who understand Zcash better on the planet. Big, big, big range there, but we're talking about pretty small numbers in absolute terms.

**SPEAKER_00:**
[02:08] Yeah, exactly. I say if Jim's not an expert, I don't know what even expert means. Anyways, Kiran, do you want to give a quick intro of yourself before we—

**SPEAKER_02:**
[02:18] Certainly. I'm our CEO. Been on these before. By the way, Vicky, we're letting Jim off the hook calling him a special guest. He has to do this all the time now with our continued in the public press.

**SPEAKER_00:**
[02:32] Okay. Special now, not special in the future. Special today. Today is special, but it's the first of many. Let's just say that. I was looking through the prior videos.

**SPEAKER_03:**
[02:46] Jim has never appeared on one of our own spaces. He's only been on early days of—

**SPEAKER_00:**
[02:52] Older drinks. Well there you go. Oh no, you found out. But it won't be special soon. Bob, by the way, since you've spoken up, can you give that quick intro to yourself?

**SPEAKER_03:**
[03:04] So hi, I'm Bob. I'm head of ecosystem. And yeah, been doing a lot of spaces.

**SPEAKER_00:**
[03:13] Yeah, so I think, you know, to level set, because I think there's a lot of misunderstanding about what privacy is—what, how would you define blockchain privacy and why do you think it's important?

**SPEAKER_03:**
[03:26] Who's that question for?

**SPEAKER_00:**
[03:28] Could be for anyone. Whoever wants to go. Kiran, you want to kick us off?

**SPEAKER_02:**
[03:33] Okay, I'll take it. So, and for the—I assume that the viewer is pretty deep in the space, but I'll bring it down to a fairly low technical level.

[03:43] So blockchains are great. They let you move digitally scarce value from party to party. And the way that this is typically done is that you've got a big address, which is almost but not quite a public key, and you sort of sign a message that says, "I, Kiran"—but it's not Kiran because it's this address—"send, you know, three Bitcoin to Bob," and it doesn't say Bob, it's another address.

[04:10] You don't quite know who either of those parties are. However, you've got the address forever, and often it is the case that you can piece together what happened based on that address. Let's say you're on a centralized exchange which has KYC'd. It knows how to associate you to maybe a withdrawal address. It may not know down the line, but if you start to get a bunch of data points, you can kind of piece together who sent what to whom.

[04:40] And you're actually in an extremely transparent scenario where everyone's financial transactions are visible to everyone. And while it's a cryptographic technology, it's not necessarily a private technology.

[04:54] And this has been a problem both in the consumer setting—just, you know, people don't like this. Satoshi makes a comment, I believe, in the white paper saying that, you know, obviously to prevent the double-spend problem, which basically just is to ensure that it can't—I mean, can't be created or destroyed except by the agreed mechanism—obviously you need to know the whole history. And so he sees the problem as intrinsic, but some technologies come out later that maybe call that into question that we'll talk about.

[05:29] It's also an enterprise problem. So we can talk separately about our experience there. Sort of what the enterprises want is kind of the same as what the public blockchain people want, except with selective visibility.

[05:43] So they want to say you're doing like an on-chain stock trade, which is actually now starting to happen. You sort of want to know the other party has the stock. You don't necessarily want to know who the other party is, but you want to know that they acquired that stock legitimately. And then when you get it, you want to be able to pass it on legitimately in the same way.

[06:04] And then there's sometimes this extra requirement that like the regulator can see everything, you know. So you want sort of like an unlinkability of balance to person or company, but also this mass preservation property that I was talking about—can't create or destroy assets. They have to be acquired legitimately and so on.

[06:25] So it's a perennial problem and closer to solved, you know, but we can go into that shortly.

[06:32] Yeah, Bob, did you want to add anything to that?

**SPEAKER_03:**
[06:35] Yeah, so I mean, going back to those Bitcoin beginnings in the Bitcoin white paper, you know, it just talks about severing identity from transactions. But really, that's just pseudonymous, you know, not anonymous.

[06:51] And I think a lot of people didn't understand that differentiation back in those early days, and it's like, "Oh, Bitcoin's private, untrackable, you know, digital money." But, you know, very rapidly you have blockchain analytics coming in, you know, looking for correlations and patterns, and it's like, yeah, you're not getting a lot of security, you know, even if you're not reusing addresses—just normal things that people would do. There's lots of correlations and, you know, you can get unmasked that way.

[07:22] But yeah, Satoshi did talk a bit about zero knowledge. I can't remember who raised it. Somebody raised it early, and he was like, "Yeah, you know, that would be interesting if we could do that." But it was just—like a lot of that cryptography, you know, just didn't hadn't happened, you know.

[07:39] So Zcash started in 2016, and it was only around that kind of time or a little before that you started having, you know, these papers on SNARK constructions and going through all these different kind of rounds.

[07:54] So yeah, I mean, what that's meant is Bitcoin and then Ethereum following that same path, you know, they are an immutable public ledger forever. Ethereum even worse because it's an account model. So you are reusing the addresses all the time, right?

[08:10] And if your address is unmasked, you are forever doxxed. That's happened to at least one of the Ethereum founders who moved hundreds of millions of dollars out of a known address of his, which is probably not desired.

**SPEAKER_00:**
[08:24] Well, and I, you know, you guys have been talking about Satoshi, but Jim, I remember I think it's like earlier, like 2014, Vitalik was talking—like he was like, "ZK-SNARKs will fix all of this at some point in time." Do you remember that at all?

**SPEAKER_01:**
[08:39] Well, I mean, like, I think we went through a learning process about privacy, and that's sort of—we're understating this right now. Maybe it's because we put a lot of time and effort into some privacy solutions that technically worked but were a business failure, I think, is fair to say.

[08:59] And so, you know, the audience can learn from our failed mistakes in the past right now. But we sort of built—so we had heard years ago about ZK, but we sort of just—I don't know, at the time didn't get into it and said like, "Oh, this looks like overly complicated. You can get privacy through these other means."

[09:21] And we ended up building a system that allowed for sort of like quick spin-up of private chains that everything was sort of in an encrypted tunnel, and you could have these chains completely secure. Nobody else would see what was happening there.

[09:37] But long story short, you know, slow learning process. We found out that customers want everything, and to the point that it made it worthless. Like they—we would go into enterprise, we would say like, "Oh, you can set up these private channels with others," and they love that because they could sort of control that and they could control who goes in there.

[10:00] But then once everything was going through these private channels, then they wanted to be able to like transfer from private chain to private chain, and that's where everything started to fall apart. And getting things back onto the main chain became sort of this extra complicated system.

[10:17] And at the same time, customers wanted to have like full flexibility in having like extensions to Solidity where you could just like name a chain and send some money from chain A to chain B. And really, the only way to make that stuff work is you have to go back to ZK.

[10:36] So ZK is overly complicated, but it is necessary. And so we started looking at that again, but I think like the safe thing to do is start with a proven technology. And Zcash had been around for years and nobody had stolen money.

[10:54] And this is just sort of like a subset of ZK, but it's kind of a cool thing. You can build what they call tumblers of money. You throw a bunch of money in, and then the money that you put into the tumbler is—you know how much went in, but the ownership is completely scrambled up.

[11:12] And at any time you can go and transfer money from within the tumbler from one user to another. But only the users who did the transferring and got the money know what was there, but nobody else can see what's happening. So again, like you have these systems of multiple users with lots of money, but you don't know who owns percentage of the money.

**SPEAKER_00:**
[11:34] Yeah, actually, before we even go that far, can we talk just like what is ZK and how does it work, and why is it an important part of the solution? I want to pull back for a second.

**SPEAKER_02:**
[11:44] I remember—I think there was an Ethereum meetup in New York. I'm not sure if either you guys were there. I think I spoke at it maybe. And there was also a Zcash, I think, presentation there.

[11:56] And it was at that time taking seven minutes to generate the ZK proofs. So—

**SPEAKER_00:**
[12:02] Yes.

**SPEAKER_02:**
[12:03] Yeah, wanted to make a transaction, you'd do this thing, it took seven minutes, and then the verification was kind of fast. Once you had it and you sent it to the network, things could go on, you know. But the usability was not there in those days. This is part of the reason we weren't like going to tell our enterprise customers, "Oh yeah, let's ZK everything," you know. Even if we had it all integrated nicely, there's a lot of devil in the details.

**SPEAKER_01:**
[12:29] I know it was unbelievably slow for a while, and I think it's fixed. But—

**SPEAKER_02:**
[12:34] Yeah, I know.

**SPEAKER_01:**
[12:35] Well, it's complicated. I mean, this is what I was trying to say before. It's like, I have sort of nuts and bolts experience of what's going on in Zcash, but the more complicated world of zero knowledge—that's my aspirational part right now. I can sort of see pieces moving within there, but I would hesitate to speak more broadly on this.

[12:57] Except let's say that it is more complicated than any of the, like for instance, Ethereum—

**SPEAKER_00:**
[13:04] Yeah.

**SPEAKER_01:**
[13:05] —client implementation stuff that we were doing back in the day.

**SPEAKER_00:**
[13:08] Yeah, yeah. Can you give a high-level summary of what zero knowledge is? Like I think very few people understand.

**SPEAKER_02:**
[13:14] I have a good layman example. Okay, and Jim can correct me. So I did take a theoretical cryptography class, and the example they bring up is the CEO problem, so to speak. So we got two CEOs, and they're high-ego guys, you know?

[13:31] And they want to know—

**SPEAKER_00:**
[13:33] Do you speak from experience, Kiran, or yeah?

**SPEAKER_02:**
[13:36] Yeah, let's think about myself. They want to know who has the most between the two, but they don't want to know how much money. They merely want to know which one has more.

[13:48] And you would think that there wouldn't really be a way to create a scheme in which they could learn that information and nothing else, but there actually is. And again, this is almost ten years ago now, so I may be describing the example incorrectly.

[14:04] But yeah, that's like a case where you might want zero knowledge. Similarly, like, you know, like an ID check in a bar. You're leaking all your personal info when you hand the ID to the bouncer—your home address, your full name, your date of birth, you know, et cetera.

[14:20] So you may want to prove to the bar that you're 21 without handing any other info over, basically. I think this is the general setting that it ends up at. Jim, do you want to take it, run with it, correct it?

**SPEAKER_01:**
[14:34] Yeah, so this is—when you first look up zero knowledge, there are lots of little examples like this. They're all pretty cool. But what's really happening in Zcash is that what you're trying to do is pass money from person A to person B.

[14:50] And person A wants to prove to person B that they have the money and that it was actually transferred, but without giving away the amount of money that person A has or without person A learning how much that person B has. Just that, you know, that the state before was that you had the amount and that the state after is that it was transferred over.

[15:13] And then also no one else in the world can know this. So you're proving sort of the important parts, not others.

[15:21] Zero knowledge could get pretty complicated too, because when you start looking into it, there are a lot of one-off examples like you're talking about that you sort of see a solution to. But the problem comes about in trying to come up with a sort of a generic solution where you can almost just compile any amount of code into some ZK proof and then run that for anything.

[15:46] I don't remember because it's been about a year now, but in Zcash there were multiple—multiple zero knowledge proofs in there for various aspects. If I were—you know, I might be making up some of the details here, but I think there was like one proof was like to show that you had more than such and such money before the transfer. I might have it slightly off, but there were multiple of these zero knowledge algorithms in there.

[16:14] But put together, they allowed for the full sort of transfer of money within the tumbler. And each one sort of had been worked out independently of each other using a more generic system where they compiled certain algorithms in there.

[16:29] Does that make sense? So making it generic can get really complicated.

**SPEAKER_02:**
[16:35] Terminology for the listener that you've heard that I barely remember: So SNARKs and STARKs were a thing that Vitalik was talking about a lot and still does. So it's like Succinct, Non-interactive, Arbitrary—something—compute—I can't remember.

**SPEAKER_01:**
[16:51] Interactive proof, yes.

**SPEAKER_02:**
[16:53] But what's the whole acronym? But so there is a way, I think, to take an arbitrary computation and to prove that it has a certain result without revealing like the intermediate states and so on. But it's not computationally feasible, like—or it's just so slow that if you try to do it that way, it becomes very difficult.

[17:16] So I believe—just tying back to Jim's point—like you could try to do this in generality. Like the EVM—like there are ZK-EVMs. Like I can verify any computation that comes out of this thing. And I think the problem with them has been performance.

[17:33] And so the Zcash people, I guess, had to decompose every little step into specific ZK circuits, right? Like, or—

**SPEAKER_01:**
[17:42] Yeah, yeah.

**SPEAKER_02:**
[17:43] So yeah, it's very, very low-level programming thinking in the ZK world. Like literally there's circuits that you end up compiling and so on and so forth.

**SPEAKER_01:**
[17:52] Yeah, Zcash at the moment is on to its fourth iteration today. And sort of by identifying a certain set of algorithms and just focusing on them, they were able to sort of solve this one tumbler problem without going any more in-depth than that.

[18:08] So this isn't like—in the dream world you would take any like Ethereum contract and compile it somehow as a, you know, something zero knowledge and then prove that you had run the full contract. That's something that at the time, at least so far in the world as it is, I didn't want to get into it or have us get into the company.

[18:32] But just to have these tumblers in place, I think that solves a lot of—

**SPEAKER_03:**
[18:37] Yeah, Bob, you were saying something?

[18:40] Yeah, so Zcash is onto its fourth round of different cryptography. So I forget what they're called—Sapling, something else. We're onto Orchard now. But I mean, that's been now over the course of nearly a decade. You know, each time you've got another sort of two years worth of leading-edge advancement.

[18:59] And yeah, like talking about that performance thing—so it's something which I think has been a key piece in Zcash price appreciation recently has been the arrival of a functional mobile wallet. So that's called Zashi, which is made by the Electric Coin Company.

[19:18] But you're basically at the point where you can run that proof on your phone. So something which used to be laptop, seven minutes, is now phone, second.

[19:28] So what you've seen, if you look at the size of these shielding pools—where these pools are effectively like, you know, all of these things are all, you know, mixed and hidden together, right? The more that you've got in a pool, the more, you know, and the more unlinkable you are.

[19:47] If you have—you know, if you do something simple like ring signatures where you just—whatever—I think Monero has got 16 transactions that, you know, get all joined together, so you can trace through that to a degree.

[20:02] But if you've got, you know, hundreds or thousands or millions of people in that same pool, you know, it's effectively, you know, completely anonymous at that point.

[20:13] But if you look at the stats of usage of these particular pools—are you seeing what proportion of the money supply has been shielded versus being transparent? I guess that's just another thing to say, right, is Bitcoin is transparent, you know, same with Ethereum, but then they use the word "shielded" to talk about, you know, that you are within this anonymity set.

[20:38] So these earlier rounds, you know, you had a bit of use but not a ton of use. But right now, I can't find the view, but it was something like about four or five million of the 21 million were within that shielding pool.

[20:52] So, you know, a significant chunk of it is shielded now, which was never the case in the past, you know. I remember on ETC at some point we were looking at whether we were going to bring over the precompiles to do with some of the curves, you know.

[21:08] I don't know if you remember that happened in Ethereum at some point, but one of the—like curves, I think, went into the precompile. And we were talking about whether we were going to like do that or not. And really talking about gas limit as well, you know, like how gas-expensive would operations be using these things even.

[21:27] And the stats at that time were, you know, it's like maybe 2% of transactions on Zcash were shielded, something like that. You know, it's basically like not being used at all, you know, functionally pretty much identical to Bitcoin.

[21:41] But probably a lot of Venus is going, "Yeah, I'm using Zcash, I'm private." It's like, yeah, you know, you're not—not at all. You're getting zero benefit at all.

[21:49] But yeah, that's really happening now. And I think it's just, you know, these rounds and rounds of years and years of research and then implementation of those and engineering effort, and it's like, hey, it works now.

**SPEAKER_00:**
[22:02] Well, I'm just curious from your standpoint, Jim, like is it a technological advancement that has created it, or is it just simply that these tumblers have gotten big enough that they offer real privacy? Do you know what I mean?

**SPEAKER_01:**
[22:14] It's—I mean, any of these things are technological advancements. But I mean, you want to have the tumblers big enough so that you have some amount of anonymity within there. It's not like if it's a tumbler of one person, then it's not much of a tumbler.

**SPEAKER_02:**
[22:28] I need to interject. I have a crypto friend who was texting about thirty seconds ago about whether I like Zcash at this price. This is a pre-recorded podcast, so, you know—well, I guess it'll run on Wednesday, November 12.

[22:44] But very timely, you know, I think. It's sort of like—I again, there's the old crypto joke where like when your dentist and realtor friends start asking you about Ripple and Cardano, it's time to unwind your positions a little bit, you know.

[23:00] But it's the Zcash meta. I don't know, like maybe that means there's room to run. Like maybe maybe it tops.

**SPEAKER_00:**
[23:08] Well, as they say, it's like catching a falling knife, right? Like, you know, like trying to figure out the peak of the market.

[23:15] Okay, like we've talked about kind of how Zcash works and it uses ZK in these sort of very specific areas, and it's not, you know, programmable generally. Now, obviously there's a lot of talk in the Ethereum world about ZK-EVMs. You guys have any thoughts on that and like, you know, how those work?

[23:35] Because, you know, at what point do we get—like is it truly impossible to get full programmability, or is that something that is just getting closer?

**SPEAKER_02:**
[23:44] From a market perspective, I think they're mostly—ZK-EVMs have been used for scaling as opposed to privacy. Even there, you tend to see some amount of specificity.

[23:55] Like, I think I mentioned on a podcast before, I'm, you know, friend-acquaintances with the Lyra CEO, and Lyra uses—Lyra is like the L2 version of Hyperliquid, if you will, where they do perps and they do zero-knowledge matching off-chain, but you know it actually works and it gets written to Ethereum, which is pretty cool.

[24:17] And supposedly they're achieving really high throughputs this way. It's not necessarily privacy tech at all.

[24:24] I ran into some of the Aztec folks in Singapore, and it seems—trending general-purpose, still on testnet, but not fully VM. It's like a restricted UTXO-type language of sorts, I believe.

[24:39] So I think there's probably—not being nearly as expert as Jim, who I'll defer to in a second—not being an expert, I think it will be—there's no intrinsic reason you can't make it fully VM or full Rust or some, you know, JavaScript or whatever.

[24:56] But probably there will be a tremendous amount of optimization that would have to happen to make that happen. So you probably see special-purpose for a while.

**SPEAKER_03:**
[25:06] I saw that—and now I'm blanking on the name—the ZK tech that was happening under the Polygon banner with—and I can't remember the name of the project now. They posted it within the last few months that they were real-time ZK proving mainnet now.

[25:24] But, you know, it was with a battery of GPUs. It was not a thing that you would be doing yourself. But yeah, that full proving is, you know, is possible. But yeah, you have that optimization to be done.

[25:40] But I mean, I think that's where things are going to end up—that you've had this sort of improvement where, starting at Bitcoin, it's like, well, how are we going to prove—get to global consensus and solve the double-spend problem? Well, it's by publishing all the details, and then we're going to have, you know, redundant state machines running in parallel, right?

[26:01] And that's the answer we know that works. It was like, you know, Satoshi did the big ugly thing, but it worked and it made this stuff possible that had never been possible before. But it is, you know, it's an incredibly big, ugly, expensive way of doing that.

[26:18] And then I think just over time it's like, okay, well, having things public was sort of a requirement for that consensus model, but that was never intentional, like having them all as a public ledger. Like that's not a positive feature.

[26:34] Now if you look at the cypherpunk culture that many of these people were coming out of, yeah, it's private, unstoppable money. Yeah, no, it wouldn't be public.

[26:43] So I saw that—yeah, within weeks of Bitcoin starting, Hal Finney said, you know, looking at ways of improving anonymity in Bitcoin. So that was January 2009. You know, that was a cypherpunk's obvious first reaction is, yeah, this is cool now. But yeah, we should have privacy as well.

[27:03] And I think we're sort of getting to that point of the tech has become good enough to solve that without broadcasting everything to everyone.

**SPEAKER_00:**
[27:14] Yeah, Jim, what do you think? Like, you know, on the sort of general programmability ZK front.

**SPEAKER_01:**
[27:21] I wish I had more, you know, hands-on experience with general ZK. I see a lot of people very excited by it, and maybe in a way that makes me skeptical because it seems like a cool toy. But I am open to them working great.

[27:39] And so I don't want to make a strong firm stance at the moment on them, but they would be great if they work.

**SPEAKER_00:**
[27:48] Yeah, I—it seems like the approach, to Kiran's point, is like find specific areas where you can, you know, create circuits and apply them and optimize for those, and then expand that over time, you know. Like it's really about kind of like, you know, nailing those initial use cases and using the dispatch approach.

**SPEAKER_01:**
[28:07] And that's why I was drawn to that, because if you really narrow it down to something really simple, then I think you can do it well.

**SPEAKER_02:**
[28:16] I've heard that people even—maybe compile the specific circuits and then optimize. Like you kind of write them with the general tool. Some people do, I don't know. And then you kind of like, okay, I got the circuit for the specific thing, but then I got to make it like work, you know.

**SPEAKER_00:**
[28:33] Yeah, maybe. I think compiling a circuit is still pretty—very like computational-intensive, but it's way more—but it's way less for most circuits. Once a circuit is compiled, it's way less to do the proof, which is, you know—and you've got to continue to push that down, but I think the ratio is very large.

[28:54] Okay, well, I think we are out of time. You know, where can we find you, Jim? I'm going to start with you. Where can people find you?

**SPEAKER_01:**
[29:03] Find me? Yes, people want to hear more and learn more about Jim, which I, you know, please speak up. Ask him where they can find you.

[29:12] I do have a Twitter handle. What is my Twitter handle? I can't remember, but—

**SPEAKER_00:**
[29:17] Probably J or model. I guess it's probably—

**SPEAKER_02:**
[29:20] I'm going to try to check. Hold on.

**SPEAKER_01:**
[29:23] Yeah, but whatever it is, you should post more often than it. Okay, I—Twitter is—I like wake up one day and remember that Twitter exists, and then I tweet a lot, and then I forget about that for a couple of weeks.

**SPEAKER_02:**
[29:39] It's J-H-O in the chat. I don't know if we can all see that, the studio chat, but—

**SPEAKER_00:**
[29:45] Yeah.

**SPEAKER_01:**
[29:46] So yes, you can find him at J Hermas.

**SPEAKER_00:**
[29:49] Kiran, where can people find you?

**SPEAKER_02:**
[29:51] Yeah, oh, J Hermas. Yeah, I'm on X, K-G-Ruben. I'm also on Substack trying to, you know—I'm like a couple old Medium posts that I've linked from there. I'm getting a little bit into a Substack rhythm. It'll probably be infrequent but at least of moderate to high quality.

[30:11] Also K-Gruben dot Substack, I think, for now. Maybe I'll change the URL.

**SPEAKER_00:**
[30:17] Yeah, and link it in the show notes when we start, assuming we do show notes.

[30:22] And you can find me on X at Vic4Wong. Bob has posted why I explained before in my handle. You can also find us on Telegram at the Stratum Mercado Group. Just go to our website at stratummercado.com and that will point you to Telegram.

[30:39] And Bob, where can people find you, and what can people expect next week? Don't close it out. Bob, you're the resident Zcash shill. One year from now, Zcash—

**SPEAKER_02:**
[30:51] Price or market cap or both?

**SPEAKER_03:**
[30:54] I think it will be in the top 10.

**SPEAKER_02:**
[30:57] Top 10.

**SPEAKER_03:**
[30:58] It's been very close. And the primary reason is privacy is a big need and it solved it, right? It's not some future promise. Like it works right now. There's a mobile app. People are using it, you know.

[31:13] You've got like a ten-year—nearly ten-year history of, you know, top brainiacs working on this. Lots of credibility. So, you know, I think it's great.

[31:26] And then I'm looking forward to smart contracts with that kind of level as well. Just one more thing to mention—I couldn't remember Jordi's project, Zisk. So that was—that's a spin-off group now from Polygon led by Jordi Baylina, and they announced real-time proving of mainnet blocks. That was announced at DevCon this year.

[31:49] So proving a block in seven and a half to twelve seconds, so just under block time. However, it requires 24 very high-powered GPUs or 48 more consumer-spec. So you've got a rack.

**SPEAKER_00:**
[32:06] There you go. And Bob, with that prediction, where can we find you, and can you give us a preview of what people can expect next week?

**SPEAKER_03:**
[32:14] Absolutely, yes. So I'm Bob Summerwill—Summer like the season, W-I-L-L—so on everything with that name.

[32:23] And yes, so next week we will have an Early Days of Ethereum interview with Christoph Jentzsch, formerly of ETH DEV. So he was hired in September 2014 into that Berlin office, worked on testing, cross-client testing, and then later on with their smart locks and the creation of the DAO, which is probably, you know, Ethereum's first killer app until—

**SPEAKER_00:**
[32:51] Killing in many different ways.

**SPEAKER_03:**
[32:53] Yes, we're doing that.

**SPEAKER_00:**
[32:54] Or you can say birthing because ETC came out of that, correct?

**SPEAKER_03:**
[32:58] Right.

**SPEAKER_00:**
[32:59] Okay, well, that's time. Thank you very much for joining us, and we look forward to seeing you next week. Take care.

**SPEAKER_03:**
[33:06] Thanks, everybody.