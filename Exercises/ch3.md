# Character 6

## 6.1

由$V_{t+1}(S_t) \leftarrow V_t(S_t)+\alpha [R_{t+1} +\gamma V_t(S_{t+1})-V_t(S_t)]$，

$\delta_t = R_{t+1}+\gamma V_t(S_{t+1})-V_t(S_t)$

令$\mu_{t}=\alpha [R_{t+1} +\gamma V_t(S_{t+1})-V_t(S_{t})]$

得，

$$
\begin{aligned}
    G_t-V_t(S_t) &= R_{t+1} + \gamma G_{t+1} - V_t(S_t) + \gamma V_t(S_{t+1}) - \gamma V_t(S_{t+1}) \\
    & = \delta_t + \gamma(G_{t+1}-V_t(S_{t+1})) \\
    & = \delta_t + \gamma(G_{t+1}-V_{t}(S_{t+1}) + \mu_{t+1}) -\gamma\mu_{t+1} \\
    & = \delta_t + \gamma(G_{t+1}-V_{t+1}(S_{t+1})) - \gamma \mu_{t+1} \\
    & = \delta_t +\gamma\delta_{t+1} + \gamma^2(G_{t+2}-V_{t+2}(S_{t+2})) + \gamma \mu_{t+1} +\gamma^2 \mu_{t+2}\\
    & ... \\
    & = \sum_{k=t}^{T-1}\left[\gamma^{k-t}\delta_{k} + \gamma^{k-t+1}\mu_{k+1} \right]
\end{aligned}
$$

由上，需要额外加的一项是$\sum_{k=t}^{T-1} \gamma^{k-t+1}\mu_{k+1}$

## 6.2


## 6.3



## 6.4



## 6.6



## 6.6



## 6.7



## 6.8



## 6.9



## 6.10



## 6.11


## 6.12



## 6.13



## 6.14



## 6.16

