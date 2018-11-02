# Closeness Of An Article With The Given Subject

## Usage

Update `v2/index.py` file with any subject and then paste the article in the `v2/sample_input.txt` file.

### TF IDF from wiki articles and your article

```sh
$ python index.py

Is 'Illusion' related to your context?([y]/n)
Is 'Optical illusion' related to your context?([y]/n)		
Is 'Moon illusion' related to your context?([y]/n)		
Is 'Use Your Illusion II' related to your context?([y]/n)		
Is '13 Ghosts' related to your context?([y]/n)n
Is 'Illusion (company)' related to your context?([y]/n)n
Is 'Use Your Illusion I' related to your context?([y]/n)
Is 'The Grand Illusion' related to your context?([y]/n)
Is 'Grid illusion' related to your context?([y]/n)
Is 'Auditory illusion' related to your context?([y]/n)
=======Getting data set for Illusion========
```
| key | dataset | article |
| --- | ------- | ------- |
| describ | 0.269 | 0.336 |
| normal | 0.42 | 0.56 |
| sinc | 0.0 | 0.0 |
| constanc | 0.269 | 0.336 |
| individu | 0.269 | 0.336 |
| An | 0.42 | 0.56 |
| interpret | 0.269 | 0.336 |
| share | 0.565 | 0.847 |
| distort | 0.42 | 0.56 |
| mouth | 0.565 | 0.847 |
| within | 0.42 | 0.56 |
| though | 0.128 | 0.154 |
| perceiv | 0.0 | 0.0 |
| hear | 0.42 | 0.56 |
| theori | 0.128 | 0.154 |
| perceptu | 0.42 | 0.56 |
| realiti | 0.42 | 0.56 |
| often | 0.128 | 0.154 |
| visual | 0.0 | 0.0 |
| sound | 0.42 | 0.56 |
| ventriloquist | 0.565 | 0.847 |
| base | 0.269 | 0.336 |
| form | 0.42 | 0.56 |
| true | 0.565 | 0.847 |
| motion | 0.42 | 0.56 |
| figur | 0.42 | 0.56 |
| principl | 0.42 | 0.56 |
| occur | 0.269 | 0.336 |
| without | 0.626 | 1.253 |
| would | 0.0 | 0.0 |
| biolog | 0.42 | 0.56 |
| gestalt | 0.42 | 0.56 |
| allus | 0.626 | 1.253 |
| depth | 0.42 | 0.56 |
| mysteri | 0.565 | 0.847 |
| term | 0.42 | 0.56 |
| bodi | 0.42 | 0.56 |
| condit | 0.565 | 0.847 |
| one | 0.0 | 0.0 |
| sensat | 0.42 | 0.56 |
| thi | 0.128 | 0.154 |
| watch | 0.42 | 0.56 |
| abl | 0.565 | 0.847 |
| physic | 0.0 | 0.0 |
| run | 0.565 | 0.847 |
| absenc | 0.565 | 0.847 |
| organiz | 0.565 | 0.847 |
| use | 0.0 | 0.0 |
| come | 0.42 | 0.56 |
| for | 0.0 | 0.0 |
| optic | 0.0 | 0.0 |
| see | -0.117 | -0.134 |
| gener | 0.269 | 0.336 |
| exampl | 0.0 | 0.0 |
| assumpt | 0.42 | 0.56 |
| these | 0.42 | 0.56 |
| environ | 0.269 | 0.336 |
| disambigu | 0.565 | 0.847 |
| word | 0.626 | 1.253 |
| illus | -0.117 | -0.134 |
| creat | 0.42 | 0.56 |
| reveal | 0.269 | 0.336 |
| other | 0.269 | 0.336 |
| domin | 0.565 | 0.847 |
| auditori | 0.269 | 0.336 |
| viewer | 0.565 | 0.847 |
| movement | 0.565 | 0.847 |
| structur | 0.565 | 0.847 |
| hallucin | 0.42 | 0.56 |
| some | 0.565 | 0.847 |
| dummi | 0.565 | 0.847 |
| sensori | 0.42 | 0.56 |
| vision | 0.128 | 0.154 |
| percept | 0.269 | 0.336 |
| brain | 0.128 | 0.154 |
| outsid | 0.565 | 0.847 |
| the | -0.117 | -0.134 |
| speech | 0.626 | 1.253 |
| human | 0.128 | 0.154 |
| made | 0.565 | 0.847 |
| organ | 0.269 | 0.336 |
| transpar | 0.626 | 1.253 |
| refer | 0.0 | 0.0 |
| make | 0.128 | 0.154 |
| stimulu | 0.269 | 0.336 |
| sourc | 0.42 | 0.56 |
| sens | 0.269 | 0.336 |
| capac | 0.565 | 0.847 |
| stimul | 0.42 | 0.56 |
| may | 0.269 | 0.336 |
| specif | 0.269 | 0.336 |
| articl | 0.626 | 1.253 |
| water | 0.42 | 0.56 |
| hand | 0.626 | 1.253 |
| misinterpret | 0.565 | 0.847 |
| unlik | 0.42 | 0.56 |
| understood | 0.565 | 0.847 |
| wherea | 0.42 | 0.56 |
| regardless | 0.42 | 0.56 |
| peopl | 0.565 | 0.847 |
| work | 0.128 | 0.154 |
| dial | 0.626 | 1.253 |
| emphasi | 0.565 | 0.847 |
| voic | 0.42 | 0.56 |

```sh
Average tf-idf distance error of the given article:0.17011218227932393
```

## Help Needed

1. For only few keys, we have got negative `tf-idf` which shouldn't have been the case.
2. Need to make it portable package, putting more abstraction.

