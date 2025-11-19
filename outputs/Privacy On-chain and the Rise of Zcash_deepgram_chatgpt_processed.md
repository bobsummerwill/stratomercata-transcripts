**SPEAKER_00:**
[00:01] Okay. Welcome, everyone.
[00:03] We have a very special and very timely topic today: privacy on-chain and the rise of Zcash.
[00:08] And we sort of have a special guest today. So I'm Victor Wong. I am founder and Chief Product Officer at BlockApps.
[00:14] I'll get to our normal guests, but today we have Jim.
[00:17] Do you want to give us a quick intro?

**SPEAKER_01:**
[00:19] Yeah. I've known Victor and Kiran for years.
[00:22] I'm one of the founders of BlockApps and CTO.

**SPEAKER_00:**
[00:25] And you're here in particular because I would call you a Zcash expert, having written your own Zcash client.

**SPEAKER_01:**
[00:30] Well, I think I'm more aspirational at this point in time.
[00:33] I mean, the way I learn about things is I try to—

**SPEAKER_02:**
[00:36] What's that? More expert people do you think there are on, say, Zcash in particular, on the planet?

**SPEAKER_01:**
[00:40] No. The problem that I have is that I was sort of halfway in the learning process last year.
[00:45] The way I learn about things is I try to write a client for it.
[00:48] So I was doing that, but then we got pulled in different directions.
[00:51] I got to the point where I had sort of replicated the actual client that could connect.
[00:55] It would bring the data in. It would bring the proofs in.
[00:58] But just about when I was getting to the good parts, that's when we moved on to other things.

**SPEAKER_00:**
[01:03] Well, we're going to put the number—answer my other question. Put the number at between like 10 and 100.
[01:08] Maybe 10.
[01:09] I would say there's definitely fewer than 20 people who have written their own Zcash clients. Probably.

**SPEAKER_01:**
[01:13] Well, yeah.
[01:14] There's probably some core contributors.

**SPEAKER_02:**
[01:16] I imagine there’s more than a handful into Zcash.
[01:19] But when Jim says "non-expert," you know, it's like—let's say, yes. I'll expand the range: 5 to 100 people who understand Zcash better on the planet.
[01:28] Big, big range there, but we're talking about pretty small numbers in absolute terms. So, yeah.

**SPEAKER_00:**
[01:32] Yes, exactly. I say if Jim's not an expert, I don't know what expert even means.
[01:37] Anyways, Kiran, do you want to give a quick intro of yourself?

**SPEAKER_02:**
[01:40] Certainly. I'm our CEO, been on these before.
[01:43] By the way, Vicky, we're letting Jim off the hook calling him a special guest.
[01:47] He has to do this all the time now with our continued appearances in the public press.

**SPEAKER_00:**
[01:51] Special now. Not special in the future.
[01:54] Special today. Today is special, but it’s the first of many. Let’s just say that.
[01:58] I was looking through the—

**SPEAKER_03:**
[01:59] The prior videos.
[02:00] Jim has never appeared on one of our own Spaces.
[02:03] He's only been on early days of the year.

**SPEAKER_00:**
[02:05] Older drinks. Well, there you go.
[02:08] Oh no! You found out.
[02:10] But it won't be special soon.
[02:11] Bob, by the way, since you've spoken up, can you give that quick intro?

**SPEAKER_03:**
[02:13] Sure. Hi, I’m Bob. I’m Head of Ecosystem.
[02:15] And yeah, been doing a lot of Spaces.

**SPEAKER_00:**
[02:16] Yeah. So I think to level-set, because I think there’s a lot of misunderstanding about what privacy is—
How would you define blockchain privacy, and why do you think it’s important?

**SPEAKER_03:**
[02:28] Who’s that question for?

**SPEAKER_00:**
[02:30] Could be for anyone. Whoever wants to go.
Kiran, want to kick us off?

**SPEAKER_02:**
[02:33] Okay, I’ll take it.
And I assume that the viewers are pretty deep in the space, but I’ll bring it down to a fairly low technical level.

[02:39] So blockchains are great: they let you move digitally scarce value from party to party.
[02:43] And the way this is typically done is that you’ve got a big address—which is almost, but not quite, a public key—
and you sign a message that says, "I, Kiran" (but it’s not ‘Kiran,’ it’s this address), send 3 Bitcoin to Bob (and again, it doesn’t say ‘Bob’, it’s just another address).
[02:57] You don’t quite know who either of those parties are.

[03:00] However, you’ve got that address forever.
And often you can piece together what happened based on that address.
[03:05] Let’s say you’re on a centralized exchange, which is KYC’d—it knows how to associate you to maybe a withdrawal address.
[03:10] It may not know down the line, but if you start to get a bunch of data points, you can kind of piece together who sent what to whom.
[03:17] And you’re actually in an extremely transparent scenario where everyone’s financial transactions are visible to everyone.
[03:24] And while it’s a cryptographic technology, it’s not necessarily a private technology.

[03:29] And this has been a problem both in consumer settings—people don’t like this—
[03:33] Satoshi makes a comment, I believe, in the whitepaper, saying that, obviously, to prevent the double-spend problem—
which is just ensuring that value can’t be created or destroyed except by the agreed-upon mechanism—
obviously you need to know the whole history.

[03:47] And so he sees the problem as intrinsic.

[03:49] But some technologies come out later that maybe call that into question, which we’ll talk about.

[03:53] It's also an enterprise problem.

[03:54] So we can talk separately about our experience there.

[03:56] Enterprises kind of want the same things as public blockchain participants, except with selective visibility.

[04:02] So let’s say you’re doing an on-chain stock trade, which is actually now starting to happen.

[04:06] You wanna know that the other party has the stock—but not necessarily who they are.

[04:10] But you want to know that they acquired the stock legitimately, and that when you get it, you can pass it on legitimately in the same way.

[04:16] And sometimes there’s an extra requirement that regulators can see everything.

[04:20] So what you want is unlinkability of balance to person or company, but also a mass preservation property: assets can't be created or destroyed arbitrarily.

[04:30] They have to be acquired legitimately, and so on.

[04:32] So it’s a perennial problem—and closer to being solved.

[04:35] We can go into that shortly.

[04:37] Bob, did you want to add anything to that?

**SPEAKER_03:**
[04:39] Yeah, so, going back to those Bitcoin beginnings in the whitepaper—
[04:42] It talks about severing identity from transactions, but that's really pseudonymous, not anonymous.

[04:48] I think a lot of people didn’t understand that distinction early on.
[04:51] It was like, “Oh, Bitcoin is private, untrackable digital money.”

[04:55] But very rapidly, blockchain analytics firms came in, looking for correlations and patterns.
[05:00] And it became apparent that you’re not getting a lot of privacy—
even if you’re not reusing addresses.

[05:05] Just normal user behavior has lots of correlations, and you can get unmasked that way.

[05:10] Satoshi did talk a bit about zero-knowledge. I can’t remember who raised it—
somebody raised it early—and he said, “Yeah, that would be interesting if we could do that.”

[05:18] But a lot of that cryptography just hadn’t happened yet.

[05:21] Zcash started in 2016, and it was only around that time or just before that you started to have papers on zk-SNARK constructions.

[05:29] Going through all these rounds of cryptographic proofs.

[05:32] Bitcoin and then Ethereum followed the same path: transparent, immutable public ledgers.

[05:37] Ethereum is actually worse because it uses an account model—so you’re reusing addresses all the time.

[05:42] If your address is unmasked, you are forever doxxed.

[05:46] That happened to at least one of the Ethereum founders who moved hundreds of millions of dollars out of a known address—
probably not desired.

(Transcript continues…)