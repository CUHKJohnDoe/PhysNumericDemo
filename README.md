# PhysNumericDemo
Solving kinematics problems with numerical methods.

Some casual work... still in progress~

Get rid of that Excel, bro. This is the future!

## Background

There are *three important values, or vectors in two or three dimensional contexts* when it comes to describing the movement of a particle. Namely, **displacement**, **velocity** and **acceleration**.

All three can be written as functions of time $t$: $x(t)$, $v(t)$ and $a(t)$.

Certain mathematical relations can also be found between these three:

$$v(t)= \frac{d}{dx} x(t)$$

$$a(t)= \frac{d}{dx} v(t) = \frac{d^2}{dt^2} x(t)$$

## Numerical Method

Given sufficiently small $\Delta t$, we can:

+ ... estimate $\frac{dx}{dt}$ with $\frac{\Delta x}{\Delta t}$, which is:

$$\frac{x_(pre)+v_(pre)}{\Delta t}$$

+ Or, estimate $\frac{dv}{dt}$ with $\frac{\Delta v}{\Delta t}$, which is:

$$\frac{v_(pre)+a_(pre)}{\Delta t}$$

## Work in Progress

The following items will likely be appended some point in the future:

+ Generating data of displacement and velocity by a *varying* acceleration presented as a function of time.

+ 2D and 3D numerical analysis of displacement, velocity and acceleration.

+ Exporting as Excel document.
