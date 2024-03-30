#!/bin/bash

# Define the file containing the list of domains
DOMAINS_FILE="domain_list.txt"

# Define the SSH port
PORT="22"

# check password authentication for a single domain
check_password_auth() {
    DOMAIN="$1"
    password_auth=$(ssh -p $PORT -o BatchMode=yes -o ConnectTimeout=5 $DOMAIN 'grep "^PasswordAuthentication" /etc/ssh/sshd_config | awk "{print \$2}"')
    
    if [[ "$password_auth" == "yes" ]]; then
        echo "Password authentication is enabled on $DOMAIN"
        echo $DOMAIN >> SSH_AUTH_ENABLED.txt
    elif [[ "$password_auth" == "no" ]]; then
        echo "Password authentication is disabled on $DOMAIN"
    else
        echo "Unable to determine password authentication status on $DOMAIN"
    fi
}

# Export function for use with parallel
export -f check_password_auth

# Check if the domains file exists
if [ ! -f "$DOMAINS_FILE" ]; then
    echo "Error: Domain list file '$DOMAINS_FILE' not found."
    exit 1
fi

# Read the domains from the file and execute the check_password_auth function in parallel for each domain
parallel -j 5 check_password_auth ::: "$(cat "$DOMAINS_FILE")"
