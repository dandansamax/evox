import jax
import jax.numpy as jnp
from jax import random
from maf import *

key = random.PRNGKey(1)
data = jnp.load("data.npz")['X']
data = jnp.array(data)
[n, d] = data.shape
m = 6
# key = jax.random.PRNGKey(12345)
keys = jax.random.split(key, 16)

maf = MaF15(d=d, m=m)
if d != maf.d:
    if d < maf.d:
        pad_width = [(0, 0), (0, int(maf.d - d))]
        data = jnp.pad(data, pad_width, mode='wrap')
    else:
        data = data[:, :maf.d]
state = maf.init(keys)
# state = maf.setup(keys)
f, new_state = maf.evaluate(state, data)
# f, new_state = maf.pf(state)
print(f.shape)
print(f)

# maf2 JIT没过 maf11 getPF JIT没过, maf12 evaluate too slow!, maf14 JIT 没过, maf15 JIT没过
# maf15 finish