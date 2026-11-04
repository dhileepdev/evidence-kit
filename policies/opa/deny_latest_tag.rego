package policy

deny contains msg if {
	input.container.image_tag == "latest"
	msg := {
		"policy_id": "deny.latest-tag",
		"severity": "HIGH",
		"control": "CM-9",
		"message": "Container image uses the latest tag",
	}
}
