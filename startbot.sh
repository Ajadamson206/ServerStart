#!/bin/bash

function startServerStat()
{
    echo "" > nohup.out
    nohup python3 serverStat.py & 
    echo $! > botPID.txt
}

startServerStat

