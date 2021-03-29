### A small memory footprint to save query time.

Bloom filter is reperesented in memory as very tiny data with 0 and 1.

- Think of it as an array of `64` bits where all the bits are set to `0` at start.
- As we start to add rows we can set bit of `Hash(key)%64` to `1`
- So, whenever we want to query the key we can check the value at bit location `Hash(key)%64`
  - If it's 0 then the key do not exists
  - If it's 1 then there is a chance that it can exist because there is a chance that `Hash(key2)%64` may have been the same, collision


### Where does it not help?
- If all the bits in the Bloom Filter is set to 1 then there is no use of it. But, increasing it at the same time means increasing memory footprint.