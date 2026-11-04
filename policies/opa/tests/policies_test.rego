package policy_test

import data.policy.deny

test_deny_privileged_container if {
	deny[msg] with input as {"container": {"privileged": true}}
	msg.policy_id == "deny.privileged-container"
}

test_no_deny_when_not_privileged if {
	count(deny) with input as {"container": {"privileged": false}} == 0
}

test_deny_latest_tag if {
	deny[msg] with input as {"container": {"image_tag": "latest"}}
	msg.policy_id == "deny.latest-tag"
}

test_no_deny_when_tag_pinned if {
	count(deny) with input as {"container": {"image_tag": "nginx:1.25"}} == 0
}
