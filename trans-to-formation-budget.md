## Transformation Budget

$$ dV/dt = \Psi + \Omega $$

$V$ is the cumulative volume:

$$ V(\sigma) = \int_{\sigma_{min}}^\sigma v(\sigma') d\sigma' $$

and $v(\sigma)$ is the volume distribution in $\sigma$ space.

## Formation Budget

A "layer" is defined as a discrete range in density, e.g $[\sigma_1, \sigma_2]$.

The volume of that layer is:

$$ V|_{\sigma_1}^{\sigma_2} = \int_{\sigma_1}^{\sigma_2} v(\sigma') d\sigma' $$

We can see from the definition of $V$ that this is equal to

\begin{align}
V|_{\sigma_1}^{\sigma2} &= V(\sigma_2) - V(\sigma_1) \\
&= \int_{\sigma_{min}}^{\sigma_2} v(\sigma') d\sigma' - \int_{\sigma_{min}}^{\sigma_1} v(\sigma') \\
&= \int_{\sigma_{min}}^{\sigma_1} v(\sigma') d\sigma' + \int_{\sigma_1}^{\sigma_2} v(\sigma') - \int_{\sigma_{min}}^{\sigma_1} v(\sigma')
\end{align}

This shows we can construct a volume budget for the layer by subtract two transformation rates:

\begin{align}
\frac{d}{dt} V|_{\sigma_1}^{\sigma2} = \Psi(\sigma_2) - \Psi(\sigma_1) + \Omega(\sigma_2) - \Omega(\sigma_1)
\end{align}

Let's now consider a two-layer model where there is only one diving sigma--let's call this $\sigma_b$: the isopycnal boundary between the two layers.

The upper layer is given by the range $[\sigma_{min}, \sigma_b]$.

The lower layer is given by the range $[\sigma_b, \sigma_{max}]$.

We also note that

$$ \Psi(\sigma_{min}) = \Psi(\sigma_{max}) = 0 $$

$$ \Omega(\sigma_{min}) = \Omega(\sigma_{max}) = 0  $$ 

So then this is the budget for the upper layer

\begin{align}
\frac{d}{dt} V|_{\sigma_{min}}^{\sigma_b} = - \Psi(\sigma_b) - \Omega(\sigma_b)
\end{align}

And for the lower layer

\begin{align}
\frac{d}{dt} V|_{\sigma_b}^{\sigma_{max}} = \Psi(\sigma_b) +\Omega(\sigma_b)
\end{align}

