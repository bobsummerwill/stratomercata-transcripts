```
**[00:00] SPEAKER_00:** Okay. Welcome, everyone. We have a very special and very timely topic today: privacy on-chain and the rise of Zcash. And we sort of have a special guest today. So I'm Victor Wong. I am founder and Chief Product Officer at BlockApps. I'll get to our normal guest, but today, we have Jim. Do you want to give us a quick intro?

**[00:21] SPEAKER_01:** Yeah. I've known Victor and Kieran for years. I'm one of the founders of BlockApps and CTO.

**[00:27] SPEAKER_00:** And you're here in particular because I would call you a Zcash expert, having written your own Zcash client.

**[00:33] SPEAKER_01:** Well, I think I'm more aspirational at this point in time. I mean, the way I learn about things is I try to—

**[00:39] SPEAKER_02:** What's that? How many more expert people do you think there are on, say, Zcash in particular, on the planet?

**[00:44] SPEAKER_01:** No, the problem that I have is that I was sort of halfway in the learning process last year. So the way I learn about things is I try to write a client for it. So I was doing that, but then we got pulled in different directions. I got to the point where I had sort of replicated the actual client that could connect. It would bring the data in. It would bring the proofs in. But just about when I was getting to the good parts, that's when we moved on to other things.

**[01:08] SPEAKER_00:** Well, to answer my other question, put the number at between, like, 10 and 100. Maybe 10. I would say there's definitely less than 20 people who have written their own Zcash clients, probably.

**[01:18] SPEAKER_01:** Well, yeah. Yeah. There's probably some core contributors.

**[01:21] SPEAKER_02:** I imagine there's more than a handful into Zcash. But, you know, when Jim says non-expert, he—you know, it's like, there are—let's say, yes, I'll expand the range. Five to 100 people who understand Zcash better on the planet. Big, big, big range there, but we're talking about pretty small numbers in absolute terms.

**[01:38] SPEAKER_00:** Yeah. Exactly. I say if Jim's not an expert, I don't know what even expert means. Anyways, Kieran, do you want to give a quick intro of yourself before we—

**[01:46] SPEAKER_02:** Certainly. I'm our CEO. Been on these before. By the way, Vicky, we're letting Jim off the hook, calling him a special guest. He has to do this all the time now with our continued in the public press.

**[01:57] SPEAKER_00:** Okay. Special now. Not special in the future. Special today. Today is special, but it's the first of many. Let's just say that.

**[02:04] SPEAKER_03:** I was looking through the prior videos. Jim has never appeared on one of our own spaces. He's only been on early days of the year.

**[02:10] SPEAKER_00:** Older drinks. Well, there you go. Oh no, you found out. But it won't be special soon. Bob, by the way, since you've spoken up, can you give that quick intro to yourself?

**[02:19] SPEAKER_03:** So hi. I'm Bob. I'm Head of Ecosystem. And yeah, been doing a lot of spaces.

**[02:25] SPEAKER_00:** Yeah. So I think, you know, to level set because I think there's a lot of misunderstanding about what privacy is. How would you define blockchain privacy and why do you think it's important?

**[02:35] SPEAKER_03:** Who's that question for?

**[02:36] SPEAKER_00:** Could be for anyone. Whoever wants to go. Kieran, you want to kick us off?

**[02:40] SPEAKER_02:** Okay. I'll take it. So—and I assume that the viewer is pretty deep in the space, but I'll bring it down to a fairly low technical level. So blockchains are great. They let you move digitally scarce value from party to party. And the way that this is typically done is that you've got a big address, which is almost, but not quite, a public key, and you sort of sign a message that says, I, Kieran—but it's not Kieran because it's this address—send, you know, 3 Bitcoin to Bob, and it doesn't say Bob. It's another address. You don't quite know who either of those parties are. However, you've got the address forever, and often it is the case that you can piece together what happened based on that address. Let's say you're on a centralized exchange, which has KYC'd. It knows how to associate you to maybe a withdrawal address. It may not know down the line, but if you start to get a bunch of data points, you can kind of piece together who sent what to whom, and you're actually in an extremely transparent scenario where everyone's financial transactions are visible to everyone. And while it's a cryptographic technology, it's not necessarily a private technology. And this has been a problem both in the consumer setting—just for, you know, people don't like this. Satoshi makes a comment, I believe, in the white paper saying that, you know, obviously, to prevent the double spend problem—which basically just is that to ensure that it can't be created or destroyed except by the agreed mechanism—obviously, you need to know the whole history. And so he sees the problem as intrinsic, but some technologies come out later that maybe call that into question that we'll talk about. It's also an enterprise problem. So we can talk separately about our experience there. Sort of what the enterprises want is kind of the same as what the public blockchain people want, except with selective visibility. So they want to say you're doing, like, an on-chain stock trade, which is actually now starting to happen. You sort of want to know the other party has the stock. You don't necessarily want to know who the other party is, but you want to know that they acquired that stock legitimately. And then when you get it, you want to be able to pass it on legitimately in the same way. And then there's sometimes this extra requirement that, like, the regulator can see everything. You know? So you want sort of, like, an unlinkability of balance to person or company, but also this mass preservation property that I was talking about—can't create or destroy assets. They have to be acquired legitimately and so on. So it's a perennial problem and closer to solved, you know, but we can go into that shortly. Yeah. Bob, did you want to add anything to that?

**[05:17] SPEAKER_03:** Yeah. So, I mean, going back to those Bitcoin beginnings in the Bitcoin white paper, you know, it just talks about severing identity from transactions. But really, that's just pseudonymous, not anonymous. And I think a lot of people didn't understand that differentiation back in those early days, and it's like, oh, Bitcoin's private, untrackable, digital money. But, you know, very rapidly, you have blockchain analytics coming in, looking for correlations and patterns, and it's like, yeah, you're not getting a lot of security. Even if you're not reusing addresses, just normal things that people would do—there's lots of correlations and you can get unmasked that way. But yeah, Satoshi did talk a bit about zero knowledge. I can't remember who raised it. Somebody raised it early, and he was like, yeah, that would be interesting if we could do that. But it was just like a lot of that cryptography just hadn't happened. So Zcash started in 2016, and it was only around that kind of time or a little before that you started having these papers on SNARK constructions and going through all these different rounds. So yeah, I mean, what that's meant is Bitcoin and then Ethereum following that same path—they are an immutable public ledger forever. Ethereum even worse because it's an account model. So you are reusing the addresses all the time. Right? And if your address is unmasked, you are forever doxed. That's happened to at least one of the Ethereum founders who moved hundreds of millions of dollars out of a known address of his, which is probably not desired.
```