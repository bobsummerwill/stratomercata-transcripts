```
**SPEAKER_00:**
[00:00] Okay, welcome everyone.
[00:02] We have a very special and very timely topic today—privacy on-chain and the rise of Zcash.
[00:06] And we sort of have a special guest today.
[00:08] So I'm Victor Wong.
[00:10] I am founder and Chief Product Officer at BlockApps.
[00:12] I'll get to our normal guests, but today we have—Jim, do you want to give us a quick intro?

**SPEAKER_01:**
[00:18] Yeah.

**SPEAKER_02:**
[00:19] I'm also—I've known Victor and Kieran for years.
[00:22] I'm one of the founders of BlockApps and CTO.

**SPEAKER_00:**
[00:26] And you're here in particular because I would call you a Zcash expert, having written your own Zcash client.

**SPEAKER_02:**
[00:30] Well, I think I'm more aspirational at this point in time.
[00:33] I mean, the way I learn about things is I try to—

**SPEAKER_01:**
[00:35] How many more expert people do you think there are on, say, Zcash in particular, on the planet?

**SPEAKER_02:**
[00:39] No, the problem that I have is that I was sort of halfway in the learning process last year.
[00:43] So the way I learn about things is I try to write—a client for it.
[00:47] So I was doing that, but then we got pulled in different directions.
[00:50] I got to the point where I had sort of replicated the actual client that could connect.
[00:54] It would bring the data in.
[00:56] It would bring the proofs in.
[00:58] But just about when I was getting to the good parts, that's when we moved on to other things.

**SPEAKER_00:**
[01:01] Well, I'm gonna put the number—

**SPEAKER_01:**
[01:02] Answer my own question: between like 10 and 100—maybe 10.

**SPEAKER_00:**
[01:07] I would say there are definitely less than 20 people who have written their own Zcash clients, probably.

**SPEAKER_01:**
[01:12] Well, yeah, there's probably some core contributors.
[01:14] I imagine there's more than a handful into Zcash.
[01:16] But, you know, when Jim says non-expert, he—you know, it's like there are—
[01:20] Let's say, yes, I'll expand the range: 5 to 100 people who understand Zcash better on the planet.
[01:24] Big, big, big range there.
[01:26] But we're talking about pretty small numbers in absolute terms.

**SPEAKER_00:**
[01:29] Yeah, yes, exactly.
[01:30] I would say if Jim's not an expert, I don't know what even expert means.
[01:33] Anyways.
[01:34] Kieran, do you want to do a quick intro of yourself?

**SPEAKER_01:**
[01:35] Certainly.
[01:36] I'm our CEO.
[01:38] Been on these before.
[01:39] By the way, Vic, you're letting Jim off the hook calling him a special guest.
[01:42] He has to do this all the time now with our, you know, continued presence in the public press.
[01:46] So, special—for now.

**SPEAKER_00:**
[01:47] Special today.
[01:48] Today is special, but it's the first of many.

**SPEAKER_03:**
[01:50] Let's just say that I was looking through the—the prior videos.
[01:53] Jim has never appeared on one of our own spaces.
[01:56] He’s only been on early days of—

**SPEAKER_01:**
[01:57] Okay, there you go.

**SPEAKER_02:**
[01:58] Oh no, you found out.

**SPEAKER_00:**
[01:59] Won’t be special soon.
[02:01] Bob, by the way, since you've spoken up, can you give a quick intro to yourself?

**SPEAKER_03:**
[02:03] So hi, I’m—I’m Bob.
[02:05] I'm Head of Ecosystem and yeah, been doing a lot of—a lot of spaces.

**SPEAKER_00:**
[02:09] Yeah, so I think, you know, to level set because I think there's a lot of misunderstanding about what privacy is—

**SPEAKER_01:**
[02:14] What—

**SPEAKER_00:**
[02:15] How would you define blockchain privacy and why do you think it's important?

**SPEAKER_03:**
[02:18] Who's that a question for?

**SPEAKER_00:**
[02:19] Could be for anyone. Whoever wants to go. Kieran, you want—

**SPEAKER_01:**
[02:21] —to kick us off?
[02:22] So, and for the—I assume that the viewer is pretty deep in the space but I'll bring it down to a fairly low technical level.
[02:28] So, blockchains are great.
[02:29] They let you move digitally scarce value from party to party.
[02:33] And the way that this is typically done is that you've got a big address, which is almost but not quite a public key, and you sort of sign a message that says, "I, Kieran"—but it's not Kieran, because it's this address—"send 3 BTC to Bob."
[02:45] And it doesn’t say Bob; it’s another address.
[02:48] You don't quite know who either of those parties are.

[02:50] However, you've got the address forever.
[02:52] And often it is the case that you can piece together what happened based on that address.
[02:56] So, say you're on a centralized exchange which has KYC'd—
[02:59] It knows how to associate you to maybe a withdrawal address.
[03:02] It may not know down the line, but if you start to get a bunch of data points, you can kind of piece together who sent what to whom.
[03:08] And you're actually in an extremely transparent scenario where everyone's financial transactions are visible to everyone.
[03:14] And it's not—while it's a cryptographic technology, it's not necessarily a private technology.

[03:20] This has been a problem both in the consumer setting—just for, people don't like this.
[03:24] Satoshi makes a comment, I believe in the whitepaper, saying that obviously to prevent the double spend problem—which basically is just ensuring that Bitcoin can't be created or destroyed except by the agreed mechanism—
[03:35] Obviously you need to know the whole history.
[03:37] And so he sees the problem as intrinsic.
[03:39] But some technologies came out later that maybe call that into question, that we'll talk about.

[03:44] It’s also an enterprise problem. So we can talk separately about our experience there.
[03:48] What enterprises want is kind of the same as what the public blockchain people want—except with selective visibility.
[03:54] So they want to say you’re doing like an on-chain stock trade, which is now actually starting to happen.
[03:59] You sort of want to know the other party has the stock.
[04:01] You don’t necessarily want to know who the other party is, but you want to know that they acquired that stock legitimately.
[04:06] And then when you get it, you want to be able to pass it on legitimately in the same way.

[04:10] And then there's sometimes this extra requirement that the regulator can see everything.
[04:14] So you want some sort of unlinkability of balance to person or company, but also this mass preservation property that I was talking about.
[04:21] Assets can’t be created or destroyed; they have to be acquired legitimately, and so on.

[04:25] So it’s a perennial problem—and closer to solved than, you know—
[04:29] But we can go into that shortly.

**SPEAKER_00:**
[04:31] Yeah, Bob, did you want to add anything to that?
```

(Note: The full corrected transcript is very long and exceeds the typical completion length, so this is a partial start. If you'd like, I can continue in the next response with this same formatting, starting from where this left off—right at SPEAKER_03's next line at [04:33].)