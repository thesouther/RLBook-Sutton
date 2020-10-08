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

只有$V(A)$发生变化，说明该幕在A点结束。因为$\gamma=1,reward=0$，并且状态值都被初始化为0.5，所以其他的点不会变（只有A和E在第一幕的时候会变化）。
对于A点来说，改变量$0.5*(-\alpha)=-0.05$。

## 6.4

$\alpha$的至于变化不会影响对哪种算法更好的判断，因为$\alpha$足够小是TD和MC算法收敛的要求，从图上来看，算法的误差都在变得很小，满足了收敛性的要求。在长期来看，不会影响最终的最小的那个MSE的值。

所以，也不存在一个固定的alpha，使得表现比图中的更好。但是像上文中提到的，使用变化的alpha或者权重，可能会有效果。

## 6.5

TD误差曲线先下降后上升是因为alpha不够小。另外，近似函数的初始化也会有影响，将所有的状态价值初始化为同样的值，可能造成对终止状态价值函数的高估。
（参见相关章节 [https://github.com/LyWangPX/Reinforcement-Learning-2nd-Edition-by-Sutton-Exercise-Solutions](https://github.com/LyWangPX/Reinforcement-Learning-2nd-Edition-by-Sutton-Exercise-Solutions)）

## 6.6



## 6.7



## 6.8



## 6.9



## 6.10



## 6.11


## 6.12



## 6.13



## 6.14



## 6.15

