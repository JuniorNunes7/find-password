## Find Password

![Password Challenge](https://i.ytimg.com/vi/-uhKZTjIoeQ/maxresdefault.jpg)


### Configuration

```python
  get_password([
    {'code': [6, 8, 2], 'method': correct_placed, 'correct': 1},
    {'code': [6, 1, 4], 'method': correct_number, 'correct': 1},
    {'code': [2, 0, 6], 'method': correct_number, 'correct': 2},
    {'code': [7, 3, 8], 'method': correct_number, 'correct': 0},
    {'code': [7, 8, 0], 'method': correct_number, 'correct': 1}
  ])
```
- `code` - Array with the hint numbers.

- `method`
  - Use the method correct_placed to right numbers and correct placed.
  - Use the method correct_number to numbers right numbers, but wrong placed.

- `correct` - Total of correct numbers according the `method`.



#### You can test it in other challenges... [here](https://www.google.com.br/search?q=crack+the+code&tbm=isch).
