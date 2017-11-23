#!/bin/sh
cd $TRAVIS_BUILD_DIR/src
sbt ++$TRAVIS_SCALA_VERSION src
