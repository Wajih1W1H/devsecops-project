package main

deny[msg] {
  input.kind == "Deployment"
  container := input.spec.template.spec.containers[_]
  container.securityContext.runAsUser == 0
  msg := sprintf("ERREUR: Le container '%v' tourne en root (runAsUser=0) !", [container.name])
}
