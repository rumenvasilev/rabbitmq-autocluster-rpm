# RPM Spec for RabbitMQ Autocluster plugin

Plugin official homepage: http://aweber.github.io/rabbitmq-autocluster/

Tries to follow the [packaging guidelines](https://fedoraproject.org/wiki/Packaging:Guidelines) from Fedora.

# Using

Create the RPMs using one of the techniques outlined in the Build section below.

## Pre-built packages

Pre-built package is maintained via [aweber](http://aweber.github.io/rabbitmq-autocluster/). For more information, please see the [aweber/rabbitmq-autocluster](https://github.com/aweber/rabbitmq-autocluster) repository on GitHub.

### Version

The version number is hardcoded into the SPEC, however should you so choose, it can be set explicitly by passing an argument to `rpmbuild` directly:

```
$ rpmbuild --define "_version 0.6.1"
```

## Manual

Build the RPM as a non-root user from your home directory:

* Check out this repo.
    ```
    git clone <this_repo_url>
    ```

* Install `rpmdevtools` and `mock`.
    ```
    sudo yum install rpmdevtools mock
    ```

* Set up your `rpmbuild` directory tree.
    ```
    rpmdev-setuptree
    ```

* Link the spec file and create sources dir.
    ```
    ln -s $HOME/rabbitmq-autocluster-rpm/SPECS/rabbitmq-autocluster.spec $HOME/rpmbuild/SPECS/
    mkdir $HOME/rpmbuild/SOURCES/
    ```

* Download remote source files.
    ```
    spectool -g -R rpmbuild/SPECS/rabbitmq-autocluster.spec
    ```

* Spectool may fail if your distribution has an older version of cURL (CentOS
  6.x, for example) - if so, use Wget instead.
    ```
    VER="0.6.1"
    URL='https://github.com/aweber/rabbitmq-autocluster/releases/download'
    wget $URL/${VER}/autocluster-${VER}.tgz -O $HOME/rpmbuild/SOURCES/autocluster_${VER}.tgz
    ```

* Build the RPM.
    ```
    rpmbuild -ba rpmbuild/SPECS/rabbitmq-autocluster.spec
    ```

# Result

One RPM:
- rabbitmq-autocluster

# Run

* Make sure RabbitMQ is already running (necessary to enable the plugin)
* Install the RPM.
* Restart RabbitMQ server


# More info

See the [aweber.github.io](http://aweber.github.io/rabbitmq-autocluster/) website.
