#!/bin/bash

#---------------------------------------------------------------
# AutoFetcher Schedule v1.0 - AuthorTracker by Ronan C. P. Lana
#
#	- Stacking folders: stats, traffic; -- fetched by AuthorFetchTraffic
#	- Volatile folders: commits, repo, filesystem, users, .;
#
#	Runs in order:
#	- AuthorFetchRepository.py
#	- AuthorFetchRepositoryCommits.py
#	- AuthorFetchRepositoryFileSystem.py
#	- AuthorFetchRepositoryGitTreeMovement.py
#	- AuthorFetchRepositoryPatrons.py
#	- AuthorFetchRepositoryUsers.py
#	- AuthorFetchRepositoryUsersEvents.py
#	- AuthorFetchRepositoryUsersPulls.py
#
#   - AuthorFetchTraffic.py (runs manually - autorun not implemented)
#   - AuthorFetchFileSystemMetadata.py
#
#---------------------------------------------------------------

cd "C:\Nexon\HeavenMS_AuthorTracker"

state=-1
term=-1

stageIni() {
	rm -r state/state
}

stage0() {
	rm    lib/*
	rm -r lib/repo
	python.exe src/AuthorFetchRepository.py
	if [ "$?" -eq 7 ]; then
		term=1
		return
	fi

	echo "`date`: started state 1" >> state/author_log.txt
	echo "1" > state/state
	state=1
}

stage1() {
	rm -r lib/commits
	python.exe  src/AuthorFetchRepositoryCommits.py
	if [ "$?" -eq 7 ]; then
		term=1
		return
	fi

	echo "`date`: started state 2" >> state/author_log.txt
	echo 2 > state/state
	state=2
}

stage2() {
	rm -r lib/filesystem
	python.exe   src/AuthorFetchRepositoryFileSystem.py
	if [ "$?" -eq 7 ]; then
		term=1
		return
	fi

	echo "`date`: started state 3" >> state/author_log.txt
	echo 3 > state/state
	state=3
}

stage3() {
	rm -r lib/users
	python.exe   src/AuthorFetchRepositoryGitTreeMovement.py
	if [ "$?" -eq 7 ]; then
		term=1
		return
	fi

	echo "`date`: started state 4" >> state/author_log.txt
	echo 4 > state/state
	state=4
}

stage4() {
	rm -r lib/users
	python.exe   src/AuthorFetchRepositoryPatrons.py
	if [ "$?" -eq 7 ]; then
		term=1
		return
	fi

	echo "`date`: started state 5" >> state/author_log.txt
	echo 5 > state/state
	state=5
}

stage5() {
	rm -r lib/users
	python.exe   src/AuthorFetchRepositoryUsers.py
	if [ "$?" -eq 7 ]; then
		term=1
		return
	fi

	echo "`date`: started state 6" >> state/author_log.txt
	echo 6 > state/state
	state=6
}

stage6() {
	rm -r lib/users
	python.exe   src/AuthorFetchRepositoryUsersEvents.py
	if [ "$?" -eq 7 ]; then
		term=1
		return
	fi

	echo "`date`: started state 7" >> state/author_log.txt
	echo 7 > state/state
	state=7
}


stage7() {
	rm -r lib/users
	python.exe   src/AuthorFetchRepositoryUsersPulls.py
	if [ "$?" -eq 7 ]; then
		term=1
		return
	fi

	echo "`date`: started state 8" >> state/author_log.txt
	echo 8 > state/state
	state=8
}

stage8() {
	echo "Autorun schedule terminated successfully"
	echo "`date`: Autorun schedule terminated successfully" >> state/author_log.txt
	rm -v state/state
	term=2
}

stageErr() {
	echo "err $state"
	echo "`date`: FATAL ERROR (state $state)" >> state/author_log.txt

	echo -1 > state/state
	term=3
}

# verifies existence of state file
if [ ! -f state/state ]; then
	rm    lib/*
	rm -r lib/commits
	rm -r lib/diffs
	rm -r lib/patrons
	rm -r lib/repo
	rm -r lib/filesystem
	rm -r lib/users

	echo 0 > state/state
fi

#loads machine state
typeset -i state=$(cat state/state)
echo "Starting from state: $state"
echo "`date`: loaded from state $state" >> state/author_log.txt

term=0

while [ "$term" -lt 2 ]; do
	if [ "$term" -eq 1 ]; then
		#sleep for 5 min and try again
		echo "sleep"

		sleep 5m
		term=0
	fi

	case "$state" in
		-1 )
			stageIni
			;;

		0 )
			stage0
			;;

		1 )
			stage1
			;;

		2 )
			stage2
			;;

		3 )
			stage3
			;;

		4 )
			stage4
			;;

		5 )
			stage5
			;;

		6 )
			stage6
			;;

		7 )
			stage7
			;;

		8 )
			stage8
			;;

		* )
			stageErr
			;;
	esac
done

# $term exit codes: 1 -> usage limits; 2 -> achieved the objective; 3 -> abnormal situations;
if [ "$term" -eq 1 ]; then
	echo "`date`: Program has halted at bash state $state. Check API's limitations and usages available to date." >> state/author_log.txt
else
    echo "`date`: <DONE> Program has built the repository database." >> state/author_log.txt
fi

exit