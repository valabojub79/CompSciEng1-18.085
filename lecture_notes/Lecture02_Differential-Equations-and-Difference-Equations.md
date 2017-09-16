# Lecture 2: Differential Equations and Difference Equations

## Core concepts

### Approximating continuity
Calculus and differential equations deal primarily with continuous functions. 
For computational tractability, we can use discrete, finite approximations. 
We can use *analytical tools* like differentiation and **Taylor series** to 
*assess the accuracy* of our approximations. Accuracy assessments allow us 
to make informed decisions in the general **trade-off between 
accuracy and speed**.

### Order of approximation
The *order* of an approximation (e.g., "first order" or "second order") 
refers to the *degree of the associated error function*. That is, from a more 
computer science-y perspective or jargon, the "order (of growth)" of the 
error function implied by the chose approximation. We *prefer higher order* 
approximations since those will (somewhat counterintuitively) yield smaller 
error terms. This is because the *error is a function of the step size* used 
to discretize the domain for the approximation. Since the step size will be 
less than one, we'll be raising a value in (0, 1) to a higher power if we have 
an higher-order approximation/error function, and thus the error will be less.

### Second differences
- Approximate second derivatives
- Three approximation methods:
  - One-sided
    - **Forward** (e.g., f'(x) apx. by (f(x + h) - f(x)) / h)
    - **Backward** (e.g., f'(x) apx. by (f(x) - f(x - h)) / h)
  - Two-sided (**centered**): f'(x) apx. by (f(x + h) - f(x - h)) / h
- **Centered is usually preferable** because it *yields second-order error*.
- To show the difference in error order between one-sided vs. two-sided/centered 
differences, use a *Taylor series approximation* to u(x + h) and u(x - h), and 
then compare the values of the expressions for the above approximations 
to f'(x).

## Tips and tricks
- It's very helpful to **graph** systems and solutions.
