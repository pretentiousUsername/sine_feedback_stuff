> **NOTE.** I first did all this stuff around early 2024-11, including write
> this little README—I think, quite obviously, that this work could be refined
> a little bit.

Suppose we have a sinusoidal oscillator with some amount of feedback described
by a function $x:\mathbb{R} \rightarrow \mathbb{R}$. Given small steps in time, $\tau$,
$$ x(t + \tau) = \sin \left( \omega t + a x(t) \right) \,, $$
where $f(0) = 0$, $t \in [0, 2\pi]$, and $a, \omega \in \mathbb{R}$. Taking the
derivative,
$$ x'(t + \tau) = \phi'(t) \cos \phi(t) \,, $$
where $\phi \equiv \omega t + a x(t)$;
$$ \cos \left( \omega t + a x(t) \right) =
    \frac{x'(t + \tau)}{\omega + a x'(t)} \,. $$
At $t = 0$,
$$ \frac{x'(\tau)}{\omega + a x'(0)} = 1 \,. $$
Taking the limit as $\tau \rightarrow 0$,
$$ x'(0) = \frac{\omega}{1 - a} \,. $$ {#eq:initial_derivative}

Next, returning to $x'(t + \tau)$, again taking the limit as
$\tau \rightarrow 0$,
$$\frac{x'(t)}{\omega + a x'(t)} = \cos\left(\omega t + a x(t) \right) \,, $$
$$ \left( \omega + a x'(t) \right) g(t) = x'(t) \,,$$
where $g(t) \equiv \cos \left( \omega t + a x(t) \right)$. With some elementary
algebra, we find that
$$ \frac{d x(t)}{dt} = \frac{\omega \, g(t)}{1 - a \, g(t)} \,. $$
Finally, rebalancing terms, with $h(t) \equiv g(t)^{-1}$,
$$\boxed{ \diff{x(t)}{t} = \frac{\omega}{h(t) - a} \,. }$$

This equation is non-chaotic if $a \in [-1, +1)$.
