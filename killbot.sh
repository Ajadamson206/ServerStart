#!/bin/bash

function killServerStat() {
    botPID=$(cat botPID.txt)
    kill $botPID
}

killServerStat