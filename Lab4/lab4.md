My assertion is that a change in programming paradigm from an older paradigm/language/library to a more modern paradigm/language/library leads to:

- A transitional period, during which more code is written
- A period thereafter, during which time less code is written

I'm analyzing GCC to attempt to prove this.

GCC recently transitioned from being written in C to C++, thereby making the following transitions:

- From procedural to object oriented
- From the C standard library (which is quite feature poor) to the C++ standard library (which is relatively feature rich, especially with respect to collections)

I was informed by [this article](http://lwn.net/Articles/542457/) which suggests in a totally anecdotal way that GCC has benefited from both the paradigm and the new library (specifically C++'s comprehensive library of generic collections).  Moreover the aforementioned article gave me a start date for the transitional period: June 18, 2008, when [this presentation](http://airs.com/ian/cxx-slides.pdf) was given at one of GCC's summits.

I deemed the end of this transitional period to be when GCC's main trunk stopped building under pure C compilers, which occurred at the time of [this post to their mailing list](https://gcc.gnu.org/ml/gcc/2012-08/msg00015.html) (i.e. August 2nd, 2012).

I wrote a simple tool in Python which allows the output of `git --no-pager log --shortstats` to be aggregated, to obtain a high level overview of repo activity.  This yields the following results:

## Post-Transition

Commits: 18088
Insertions: 4050566
Deletions: 2238396
Duration: 903 days

## During Transition

Commits: 30170
Insertions: 8483389
Deletions: 5495633
Duration: 1506 days

## Before Transition

Commits: 88050
Insertions: 22460802
Deletions: 12568041
Duration: 7147 days

This yields the following rates:

## Post-Transition

Commits/day: 20
Insertions/day: 4486
Deletions/day: 2479
Growth/day: 2007

## During Transition

Commits/day: 20
Insertions/day: 5633
Deletions/day: 3649
Growth/day: 1984

## Before Transition

Commits/day: 12
Insertions/day: 3143
Deletions/day: 1759
Growth/day: 1384

Where "growth" is defined as deletions subtracted from insertions.

We note that because "before transition" includes periods of relatively lower activity, the number of commits per day is 40% lower.  We adjust the values to compensate:

## Before Transition (Adjusted)

Commits/day: 20
Insertions/day: 5238
Deletions/day: 2932
Growth/day: 2306

We observe from the data the following:

- During the transition period there were more insertions and more deletions, however the code base grew at a slightly lower rate, meaning that code was being replaced/rewritten as part of the transition
- After the transition less code had to be written once the rate of contribution (i.e. commits per time period) were adjusted, meaning that the paradigm/language/library shift likely paid off in terms of lower programmer workload
- After the transition the code base is growing at a slower rate than before, which will likely keep the code base manageable for longer