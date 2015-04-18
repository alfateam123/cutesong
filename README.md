CuteSong: your Python wrapper to openings.moe
=============================================

[![Build Status](https://travis-ci.org/alfateam123/cutesong.svg?branch=master)](https://travis-ci.org/alfateam123/cutesong)

## What is that?

It's a wrapper to openings.moe APIs.

## How can I install that?

```sh
git clone http://github.com/alfateam123/cutesong
cd cutesong
python setup.py install #or use "pip install ."
```

## Examples?

You can find some examples in the `scripts` folder.
I'll add some more when new features will be added.

The actual usage is the following:
```
>>> import cutesong
>>> cutesong.filenames()[0]
'Opening1-AccelWorld.webm'
>>> cutesong.list()[-1]
{'title': 'Ending 1', 'source': 'Zankyou no Terror (Terror in Resonance)', 'file': 'Ending1-ZankyouNoTerror.webm'}
```

That's all.

## Why did you do that?

I was bored, saw too much C++ and Java, and not in the right mood to translate chinese cartoons.
