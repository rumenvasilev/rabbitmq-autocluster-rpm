%if 0%{?_version:1}
%define         _verstr      %{_version}
%else
%define         _verstr      0.6.1
%endif

Summary:        RabbitMQ Autocluster plugin
Name:           rabbitmq-autocluster
Version:        %{_verstr}
Release:        1%{?dist}
License:        MPLv2.0
Group:          System Environment/Daemons
URL:            http://aweber.github.io/%{name}/
Source0:        https://github.com/aweber/%{name}/releases/download/%{version}/autocluster-%{version}.tgz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires:       rabbitmq-server >= 3.5, erlang >= 17.5

%define					debug_package     %{nil}
%define					__pluginsdir      /usr/lib/rabbitmq/lib/%{name}/

%description
A RabbitMQ plugin that clusters nodes automatically using Consul, etcd2, DNS, or natively in AWS

%prep

%setup -q -c

%pre

%install
mkdir -p %{buildroot}%{__pluginsdir}
cp -a plugins/*.ez %{buildroot}%{__pluginsdir}

%post
version=`rpm -q rabbitmq-server --info | grep Version | awk '{print $3}'`
plugin_path=`rpm -ql rabbitmq-server | grep $version/plugins/README$ | sed 's/README//'`
ln %{__pluginsdir}/*.ez $plugin_path/
rabbitmq-plugins enable autocluster
service rabbitmq-server restart

%preun
rabbitmq-plugins disable autocluster
version=`rpm -q rabbitmq-server --info | grep Version | awk '{print $3}'`
plugin_path=`rpm -ql rabbitmq-server | grep $version/plugins/README$ | sed 's/README//'`
for i in `ls %{__pluginsdir}/*.ez`; do
  inode=`ls -i $i | awk '{print $1}'`
  echo "Purging links of $i"
  find $plugin_path -inum $inode -exec rm -f {} \; -print
done

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{__pluginsdir}

%doc

%changelog
* Thu Mar 28 2013 Rumen Vasilev <ice4o@hotmail.com> - 0.6.1
- Initial build
