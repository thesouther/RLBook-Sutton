# Character 8

## 8.1

不能。
- 当n较小时，V值更新仍然很慢，还是会需要一段时间才能更新所有状态。
-    当n很大时，规划方法计算效率更高，而且它的n不太受限；并且一个状态的价值改变了，会引起链式反应，model函数会更新整条链路上的状态价值；另外Dyna-Q方法探索效率更高。

## 8.2

第一阶段，Dyna-Q+算法表现更好因为其探索性更强，更快地找到最优策略；
第二阶段，Dyna-Q+算法也是因为探索性强，所以能找到最有路径；而Dyna-Q算法即使使用epsilon-greedy算法，也无法探索足够的步数找到当前最优路径，所以其斜率很小。

## 8.3

因为Dyna-Q+算法的探索性太强，导致就算达到了最优路径，它的抖动也很强，性能会稍微有点下降。这就使得两种算法之间的距离稍微变窄了点。

## 8.4



## 8.5

参考：[https://github.com/LyWangPX/Reinforcement-Learning-2nd-Edition-by-Sutton-Exercise-Solutions](https://github.com/LyWangPX/Reinforcement-Learning-2nd-Edition-by-Sutton-Exercise-Solutions)

在随机环境中，算法要维持一个奖励分布的概率表，$p(r|s,a,s')$，在规划时，对奖励进行抽样得到。
- 衰减旧reward出现的概率；
- 在使用旧数据时，衰减alpha
- 使用少量数据进行规划，旧的奖励数据要删掉。
- 另外，由于策略不会收敛，所以alpha值应该不变。

使算法同时适应随机环境和变化的环境：
One attempt to solve the situation, (in my opinion), will be the following. 
- First, we only accept limited number of newest reward data for each pair $(S, A)$ and a constant $\alpha$ to make sure we can learn from the newest. 
- Then, maintain and track how sample means and sample variances of rewards change. 
- If we observe from statistics methods that the environment is stable, we decay the alpha, increase the limit of data size and accelerate the convergent. 
- On the other hand, if stabilization cannot be detected, newest data capacity limit and constant alpha would be always hold.

## 8.6

这会加强采样更新的优势。当后继状态分支很大，并且分布非常不均匀的时候，采样更新自然采样的结果就是样本分布不均匀的结果，那些小概率出现的样本被采样的概率也小，也就是关注更重要的后继状态。而使用期望更新，那些小概率的状态也要考虑，这在一定程度上更浪费了时间。

## 8.7

因为完整扫描一次所有的状态需要大量时间。 在进行期望更新时，每次更新状态价值改变都很明显，当b=1时，状态值更新传播的很快，而当b较大时，使用期望更新的状态价值时多个后继状态价值的求和，更加稳定，但是需要的时间更长。 这也是为什么在10000个状态时，曲线很曲折也很密集，而在1000个状态的情况下，b = 10时最光滑，而b=1时最曲折。 

实际上，如果在计算时间轴（x轴）上使用相同的比例，则下面曲线的曲折点会更宽且更粗糙。

## 8.8

见code部分


