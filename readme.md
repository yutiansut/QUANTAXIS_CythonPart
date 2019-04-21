# QUANTAXIS CYTHON


cython部分重写性能部分


- QAAccount
- QAOrder
- QAData


安装: python setup.py build_ext --inplace


简单的类型指定已经可以提速约3倍左右的性能
```

In [1]: import QUANTAXIS as QA

In [2]: import timeit

In [3]: import QAAccount

In [4]: accout_raw = QA.QA_Account('xx','x','raw', init_cash=100000000000000)

In [5]: accout_cython = QAAccount.QA_Account('xx','x','cython', init_cash=100000000000000)

In [6]: %timeit -n 20000 -r 2 accout_cython.receive_simpledeal('600000',6, 100, 1,'2019-04-20')
549 ns ± 18.1 ns per loop (mean ± std. dev. of 2 runs, 20000 loops each)

In [7]: %timeit -n 20000 -r 2 accout_raw.receive_simpledeal('600000',6, 100, 1,'2019-04-20')
1.88 µs ± 43.9 ns per loop (mean ± std. dev. of 2 runs, 20000 loops each)
```