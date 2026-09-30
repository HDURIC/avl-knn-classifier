# AVL Tree and Nearest-Neighbor Classifier

A Python implementation of an AVL tree and a k-nearest-neighbor classifier for
labeled, one-dimensional numeric observations.

## Features

- AVL insertion and deletion with rotations, parent pointers, and height tracking.
- Minimum, maximum, search, and in-order, pre-order, post-order, and level-order traversal.
- Storage of numeric observations and labels in tree nodes.
- Inverse-distance-weighted classification with distance-tie filtering.

## Run

Only the Python standard library is used. Tested on Python 3.12.14.
From this repository directory:

```sh
python demo.py
python -m unittest tests -v
```

Demo output:

```text
2.8: low
8.2: high
```

Example:

```python
from solution import KNNClassifier

model = KNNClassifier(k=1)
model.train([(1.0, "low"), (3.0, "low"), (8.0, "high"), (10.0, "high")])
print(model.classify(2.8))  # low
```

## Behavior and limitations

`train` adds observations to the existing tree. Repeated numeric values are
ignored by insertion, so an existing label is not replaced by a duplicate value.
Neighbor selection groups distances using a tolerance of `1e-10` and discards
every group containing multiple observations. It may return fewer than `k`
neighbors. Classification returns `None` when no eligible neighbors remain.
An eligible observation at effectively zero distance supplies its label directly.
Otherwise, label weights are summed as `1 / distance`; equal total weights retain
the first label encountered.

Tree operations use balancing, but neighbor selection scans all observations
and compares each distance with existing groups. Its worst-case runtime is
quadratic in the number of observations, followed by sorting the group distances.
This implementation does not provide logarithmic-time nearest-neighbor queries
or support multidimensional feature vectors.

## Files and verification

- `solution.py`: AVL tree, classifier, and supplied helper code.
- `demo.py`: small classification demonstration.
- `tests.py`: supplied CSE 331 Project 5 test suite; 18 tests passing on Python 3.12.14.

The Node class, marked scaffolding, and helper code are supplied material.
`pretty_print_binary_tree` and `svg` retain attribution to
[joowani/binarytree](https://github.com/joowani/binarytree). Confirm applicable
upstream notices before redistribution. Passing the supplied tests is not a
performance benchmark or a claim of exhaustive correctness.

## Background and attribution

Developed as a computer science coursework project. Original source comments
and attribution are preserved. Supplied scaffolding, tests, and third-party
helpers retain their existing attribution. No additional license is granted
for those materials.
