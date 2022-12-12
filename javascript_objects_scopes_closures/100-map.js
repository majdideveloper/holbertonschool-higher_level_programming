#!/usr/bin/node
const Data = require('./100-data');


newList =  Data.list.map((item, index)=> item * index);
console.log(Data.list);
console.log(newList);