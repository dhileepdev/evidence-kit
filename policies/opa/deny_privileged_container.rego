package policy

deny contains msg if {
	input.container.privileged == true
	msg := {
		"policy_id": "deny.privileged-container",
		"severity": "HIGH",
		"control": "AC-2",
		"message": "Container is privileged",
	}
}
