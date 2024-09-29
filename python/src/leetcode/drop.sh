#! /bin/sh

psql postgres -f droptables.sql | grep drop > .runner.sql && psql postgres -f .runner.sql && rm .runner.sql