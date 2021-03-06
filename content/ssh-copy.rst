===========================================
Simple Command Line Tool :code:`ssh-copy`
===========================================
:date:      09-16-2014
:slug:      osx-ssh-copy
:category:  Programming
:tags:      Command Line, bash, shell
:status:    draft



.. code-block:: bash

    #!/usr/bin/env bash
    usage() { cat <<- DOCUMENT

        $PROGNAME [-h] [-t] [-k key] [-l login] [server]

        Utility for automatically exporting ssh keys into remote servers for authentication.
        Checks $HOME/.ssh for id_rsa.pub or id_dsa.pub and appends them into
        the authorized_keys of remote host

        AUTHOR:     Sang Han
        YEAR:       2013
        VERSION:    2.4

        -h [help]
            Outputs usage directions
        -t [test]
            Runs unit tests
        -k [key]
            Specify your own public key located in $HOME/.ssh directory
        -l [login]
            Specify user login credentials


        DOCUMENT
    }

    # Global Variables
    PROGNAME="$(basename "$0")"

    function error_exit() {
        printf "ERROR due to %s"  "${1:-"Unknown Error"}"
        exit 1
    }

    function test_variables() {
        declare -a variables=(${*})
        for var in "${variables[@]}"; do
            printf "%30s = %s\n" \
                "$(tput setaf 9)\$${var}$(tput sgr0)" \
                "$(tput setaf 3)${!var}$(tput sgr0)"
        done
    }

    function install_keys() {
        # Reads the public key file with cat and then logs into ssh server
        # and appends the public key file at the end of the authorized_key file
        # within $HOME
        cat < "${PUBKEY[i]}" | \
            ssh -l "$LOGIN_USER" "$SERVER" "\
                if [ -d ~/.ssh ]; then \
                    cat >> ~/.ssh/authorized_keys; \
                else \
                    mkdir ~/.ssh; \
                    cat >> ~/.ssh/authorized_keys; \
                fi"
    }

    function check_keys() {
        # Checks $HOME/.ssh directory for default keys
        if [[ $HOME/.ssh/*.pub ]]; then
            return
        else
            error_exit "missing ssh public keys"
        fi
    }

    function check_auth() {
        # Checks if proper credentials have been given as $1. After credential has
        # been checked, will read and bind the variable.
        local CREDENTIAL=$1
        if [[ ! ${!CREDENTIAL} ]]; then
            read -p "${CREDENTIAL}:  " "${CREDENTIAL}"
        fi
    }

    function check_server() {
        SERVER=$1
        if [[ "$SERVER" =~ @ ]]; then
            LOGIN_USER=${SERVER%@*}
            SERVER=${SERVER#*@}
            return
        fi
    }

    main() {
        # Default Public Keys
        if [ -z $KEY ]; then declare -a KEY=("id_rsa" "id_dsa"); fi

        for (( i=0; i<${#KEY[@]}; i+=1 )); do
            local PUBKEY[i]="$HOME/.ssh/${KEY[i]}.pub"

            # Test Keys
            if ((TEST==1)); then test_variables KEY[i] PUBKEY[i]; continue; fi

            # Gather necessary login credentials
            if [[ -r "${PUBKEY[i]}" ]]; then
                check_auth LOGIN_USER; check_auth SERVER
                install_keys && break
            fi
        done
    }

    # Option Parsing
    declare -i TEST=0
    while getopts ":k:l:th" OPTION; do
        case $OPTION in
            I) usage
               exit 0
                ;;
            II) KEY=$OPTARG
                 ;;
            III) TEST=1
                  ;;
            IV) LOGIN_USER=$OPTARG
                 ;;
            ?) { echo "Invalid option: -${OPTARG}"; usage; } >&2
                 exit 1
                 ;;
        esac
    done
        shift $((OPTIND-1))

    if [[ "$0" == "${BASH_SOURCE}" ]]; then
        # Validate user input
        if [ $# = 1 ]; then check_server "$1"; fi; check_keys

        # Test Globals
        if ((TEST==1)); then test_variables SERVER LOGIN_USER; fi

        main
    fi
