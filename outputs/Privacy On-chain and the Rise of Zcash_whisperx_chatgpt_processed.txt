```
**SPEAKER_01:**
[00:01] Okay, welcome everyone.
[00:03] We have a very special and very timely topic today: privacy on-chain and the rise of Zcash.
[00:08] And we sort of have a special guest today.
[00:10] So I'm Victor Wong.
[00:12] I am founder and Chief Product Officer at BlockApps.
[00:14] I'll get to our normal guests, but today we have Jim.
[00:17] Do you want to give us a quick intro?

**SPEAKER_02:**
[00:20] Yeah, I'm also—I've known Victor and Kieran for years.
[00:23] I'm one of the founders of BlockApps and CTO.

**SPEAKER_01:**
[00:26] And you're here particularly because I would call you a Zcash expert, having written your own Zcash client.

**SPEAKER_02:**
[00:30] Well, I think I'm more aspirational at this point in time.
[00:33] I mean, the way I learn about things is I try to...

**SPEAKER_03:**
[00:36] How many more expert people do you think there are on, say, Zcash in particular, on the planet?

**SPEAKER_02:**
[00:40] No, the problem that I have is that I was sort of halfway in the learning process last year.
[00:43] So the way I learn about things is I try to write a client for it.
[00:46] So I was doing that, but then we got pulled in different directions.
[00:49] I got to the point where I had sort of replicated the actual client that could connect.
[00:52] It would bring the data in.
[00:54] It would bring the proofs in.
[00:55] But just about when I was getting to the good part, that's when we moved on to other things.

**SPEAKER_03:**
[00:58] Well, we're going to put the number—answer my own question—right between like 10 and 100, maybe.
[01:02] I would say there are definitely less than 20 people who have written their own Zcash clients.

[01:07] Probably—well yeah, there's probably some core contributors.
[01:10] I imagine there's more than a handful into Zcash, but you know when Jim says "non-expert," he—you know, it's like—there are, let's say, yes.
[01:15] I'll expand the range: five to 100 people who understand Zcash better, on the planet.
[01:20] Big, big, big range there. But we're talking about pretty small numbers in absolute terms.

**SPEAKER_01:**
[01:24] Yes, exactly.
[01:26] I would say if Jim's not an expert, I don't know what "expert" even means.

[01:29] Anyways, Kieran, do you want to give a quick intro of yourself?

**SPEAKER_03:**
[01:31] Certainly.
[01:32] I'm our CEO—been on these before.
[01:34] By the way Vic, you're letting Jim off the hook calling him a special guest.
[01:37] He has to do this all the time now with our continued stuff in the public.
[01:41] So special in the future—special today.
[01:43] Today is special, but it's the first of many.
[01:45] Let's just say that.
[01:46] I was looking through the prior videos.
[01:48] Jim has never appeared on one of our own spaces.

**SPEAKER_00:**
[01:51] He's only been on early days of Ethereum.

**SPEAKER_03:**
[01:53] Okay.

**SPEAKER_01:**
[01:54] There you go.
[01:55] But it won't be special soon.
[01:57] Bob, by the way, since you've spoken up, can you give a quick intro to yourself?

**SPEAKER_00:**
[02:00] So hi, I'm Bob.
[02:02] I'm Head of Ecosystem.
[02:03] And yeah, been doing a lot of spaces.

**SPEAKER_01:**
[02:06] Yeah.
[02:07] So I think, you know, to level set, because I think there's a lot of misunderstanding about what privacy is...
[02:13] How would you define blockchain privacy, and why do you think it's important?

**SPEAKER_00:**
[02:16] Who's that question for?

**SPEAKER_01:**
[02:18] Could be for anyone, whoever wants to go.
[02:20] Kieran, you want to kick us off?

**SPEAKER_03:**
[02:22] So—and I assume that the viewer is pretty deep in the space, but I'll bring it down to a fairly low technical level.
[02:27] So blockchains are great.
[02:28] They let you move digitally scarce value from party to party.

[02:31] And the way that this is typically done is that you've got a big address, which is almost—but not quite—a public key, and you sort of sign a message that says,
[02:38] "I, Kieran"—but it's not Kieran, because it's this address—"send three Bitcoin to Bob."
[02:44] And it doesn't say "Bob," it's another address.
[02:46] You don't quite know who either of those parties are.
[02:48] However, you've got the address forever.

[02:50] And often it is the case that you can piece together what happens based on that address.
[02:54] So say you're on a centralized exchange which has KYC.
[02:57] It knows how to associate you to maybe a withdrawal address.
[03:00] It may not know down the line.

[03:02] But if you start to get a bunch of data points, you can kind of piece together who sent what to whom.
[03:07] And you're actually in an extremely transparent scenario where everyone's financial transactions are visible to everyone.
[03:12] And it's not—while it's a cryptographic technology, it's not necessarily a private technology.

[03:17] And this has been a problem both in the consumer setting—just for, you know, people don't like this.
[03:21] Satoshi makes a comment, I believe in the white paper, saying that—obviously, to prevent the double-spend problem, which basically is just that...

[03:28] To ensure that Bitcoin can't be created or destroyed except by the agreed mechanism—obviously, you need to know the whole history.
[03:33] And so he sees the problem as intrinsic.
[03:36] But some technologies came out later that maybe called that into question—that we'll talk about.

[03:40] It's also an enterprise problem.
[03:42] So we can talk separately about our experience there.
[03:45] Sort of what the enterprises want is kind of the same as what the public blockchain people want, except with selective visibility.

[03:51] So say you're doing an on-chain stock trade, which is actually now starting to happen.
[03:55] You sort of want to know the other party has the stock.
[03:57] You don't necessarily want to know who the other party is.
[03:59] But you want to know that they acquired that stock legitimately.
[04:01] And then when you get it, you want to be able to pass it on legitimately in the same way.

[04:05] And then there's sometimes this extra requirement that the regulator can see everything.
[04:09] So you want sort of an unlinkability of balance to person or company, but also this mass preservation property—that I was talking about—you can't create or destroy assets.
[04:17] They have to be acquired legitimately, and so on.

[04:20] So it's a perennial problem, and closer to solved, you know—but we can go into that shortly.

**SPEAKER_01:**
[04:24] Yeah.
[04:25] Bob, did you want to add anything to that?

**SPEAKER_00:**
[04:27] Yeah. Yes.
[04:28] I mean, going back to those beginnings in the Bitcoin white paper, you know, it just talks about severing identity from transactions.
[04:34] But really, that's just pseudonymous, not anonymous.

[04:38] And I think a lot of people didn't understand that differentiation back in those early days.
[04:41] And it's like, "Oh, Bitcoin's private, untrackable digital money."
[04:45] But, you know, very rapidly you had blockchain analytics coming in, looking for correlations and patterns.

[04:50] And it's like, yeah, that's—you’re not getting a lot of security.
[04:53] You know, even if you're not reusing addresses, just normal things that people would do—there's lots of correlations, and you can get unmasked that way.

[04:59] But yeah, Satoshi did talk a bit about zero knowledge.
[05:02] I can't remember who raised it.
[05:03] Somebody raised it early, and he was like, "Yeah, that would be interesting if we could do that."
[05:06] But it was just like a lot of that cryptography just hadn't happened.

[05:09] So Zcash started in 2016.
[05:11] And it was only around that kind of time, or a little before, that you started having these papers on SNARK constructions and going through all these different kind of rounds.

[05:19] So yeah, I mean, what that's meant is Bitcoin and then Ethereum following that same path—they are an immutable public ledger forever.
[05:27] Ethereum even worse because it's an account model.
[05:30] So you are reusing the addresses all the time, right?

[05:33] And if your address is unmasked, you are forever doxxed.
[05:36] That's happened to at least one of the Ethereum founders who moved hundreds of millions of dollars out of a known address of his—which was probably not desired.
```

(Note: Output truncated for length. Please let me know if you'd like the rest.)