# SENG 371 - Robert Allan Hennigan Leahy

## Project Question

Does a change in programming paradigm translate into an increase or decrease in software quality?

## Expectations

A change in programming paradigm from one "less modern" to one "more modern" leads to the following:

-	A transition period during which more work is done no the project to effect the change
-	A period following the transition during which less work is done as the paradigm change reduces the complexity of changes

## Codebases/Systems

GCC

Specifically the switch of the GCC code base from C to C++ will be examined.

This transition is deemed to have begun with [this presentation](http://airs.com/ian/cxx-slides.pdf), given in June 2008, and ended with [this post on the GCC mailing list](https://gcc.gnu.org/ml/gcc/2012-08/msg00015.html), in August 2012.

## Methodology

1.	Gather information for raw additions/deletions during four different periods of time:  
	1.	The entire lifespan of GCC
	2.	Before the C++ transition began
	3.	During the C++ transition
	4.	After the C++ transition  
	Compare and contrast this data, and determine if the expectations hold.

## Milestones

1.	Perform analysis under first methodology (COMPLETE)
2.	Develop further methodologies

## Results

### Methodology 1

#### Post-Transition

Commits: 18088
Insertions: 4050566
Deletions: 2238396
Duration: 903 days

#### During Transition

Commits: 30170
Insertions: 8483389
Deletions: 5495633
Duration: 1506 days

#### Before Transition

Commits: 88050
Insertions: 22460802
Deletions: 12568041
Duration: 7147 days

This yields the following rates:

#### Post-Transition

Commits/day: 20
Insertions/day: 4486
Deletions/day: 2479
Growth/day: 2007

#### During Transition

Commits/day: 20
Insertions/day: 5633
Deletions/day: 3649
Growth/day: 1984

#### Before Transition

Commits/day: 12
Insertions/day: 3143
Deletions/day: 1759
Growth/day: 1384

Where "growth" is defined as deletions subtracted from insertions.

We note that because "before transition" includes periods of relatively lower activity, the number of commits per day is 40% lower.  We adjust the values to compensate:

#### Before Transition (Adjusted)

Commits/day: 20
Insertions/day: 5238
Deletions/day: 2932
Growth/day: 2306

We observe from the data the following:

- During the transition period there were more insertions and more deletions, however the code base grew at a slightly lower rate, meaning that code was being replaced/rewritten as part of the transition
- After the transition less code had to be written once the rate of contribution (i.e. commits per time period) were adjusted, meaning that the paradigm/language/library shift likely paid off in terms of lower programmer workload
- After the transition the code base is growing at a slower rate than before, which will likely keep the code base manageable for longer
