

## Data Structure
collections https://doc.rust-lang.org/std/collections/index.html

- Sequence: `[]`
- vector
```
 let mut v = vec!["a"]
 v.push("");
```
- VecDeque
```
let vdq = VecDeque::new();
vdq.push_front(); vdq.push_back();
vdq.pop_front(); vdq.pop_back();
vdq.into_iter().collect();
```
- LinkedList
- HashMap
```
let mut h = HashMap::new();
h.insert("key", "val");
h.entry(key).or_insert(val);
```
- BTreeMap

- Sets
- HashSet
- BTreeSet
- BinaryHeap -> priority queue

## Libs
clap
petgraph

### Plot
rascii
