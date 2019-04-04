#!/bin/bash

#**************************Rename below db names to regdb, userdb and amdb before hand-over*******************************
db="regdb1"

mysql -u root -D$db < 'data/rush_re-indexing_2.5.0/reg-index.sql';
