#!/bin/bash

export R_LIBS=/home/lcai/R/x86_64-pc-linux-gnu-library/3.2

#find data/cel\ files -type f | parallel Rscript mas5.R {} data/mas5/{/.}
#find data/enlarged/post_vel/ -type f | cut -f 1-4 -d / | parallel Rscript mas5.R {} data/enlarged.mas5/post_vel/{/.}

