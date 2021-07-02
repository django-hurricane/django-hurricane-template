# django-hurricane-template

A cookiecutter template focused on `Kubernets-native development` (or better yet `cloud-native development`) with
strong emphasis on the following points:
- no local configuration
- nearly no difference in local builds and production (except for some additional tooling)
- development happens within a provisioned Kubernetes-based development environment (e.g. with [unikube.io](https://unikube.io))
- traffic hits the application through services and ingress configurations
- `django-hurricane` takes care for optimal Kubernetes integration 
- PostgreSQL as database backend
- a S3-based storage system

**Important:** this template is still WIP and may not work out-of-the-box.

---

## Purpose

This project is used to scaffold a lean `> django 3.2` project structure with quite a few assumptions of
the target operation platform - Kubernetes. Please see [django-hurricane](https://github.com/Blueshoe/django-hurricane) which 
is the basis for this django project generator.

What's in:
- python >=3.9
- django >=3.2
- Blueshoes coding standards
- unikube development file

## Installation

Please install [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/):
```bash
pip install cookiecutter
```

## Usage

Create a project with
```bash
cookiecutter gh:Blueshoe/django-hurricane-template
```
and answer the questions accordingly

## Credits

This cookiecutter template is heavily inspired by [wemake-django-template](https://github.com/wemake-services/wemake-django-template).
Please check out wemake's awesome work. 