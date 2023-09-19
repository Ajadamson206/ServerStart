#!/bin/bash

function startServerStat()
{
    nohup python3 serverStat.py & 
    echo $! > botPID.txt
}

startServerStat

