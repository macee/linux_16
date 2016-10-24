#!/bin/bash

function submit_flag(){

	curl -k "https://localhost:444/submit" --data "uuid=9c80e999-217f-46af-b3f1-69d146f1e746&flag=$1"

}

function clone_repo(){
	git clone "https://github.com/JohnHammond/scripting_playground"
}


while [ 1 ];
do


	sleep 60
done
