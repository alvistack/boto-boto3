# Copyright 2023 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-boto3
Epoch: 100
Version: 1.28.22
Release: 1%{?dist}
BuildArch: noarch
Summary: AWS SDK for Python
License: Apache-2.0
URL: https://github.com/boto/boto3/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK)
for Python, which allows Python developers to write software that makes
use of services like Amazon S3 and Amazon EC2.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-boto3
Summary: AWS SDK for Python
Requires: python3
Requires: python3-botocore >= 1.31.22
Requires: python3-jmespath >= 0.7.1
Requires: python3-s3transfer >= 0.6.0
Provides: python3-boto3 = %{epoch}:%{version}-%{release}
Provides: python3dist(boto3) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-boto3 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(boto3) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-boto3 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(boto3) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-boto3
Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK)
for Python, which allows Python developers to write software that makes
use of services like Amazon S3 and Amazon EC2.

%files -n python%{python3_version_nodots}-boto3
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-boto3
Summary: AWS SDK for Python
Requires: python3
Requires: python3-botocore >= 1.31.22
Requires: python3-jmespath >= 0.7.1
Requires: python3-s3transfer >= 0.6.0
Provides: python3-boto3 = %{epoch}:%{version}-%{release}
Provides: python3dist(boto3) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-boto3 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(boto3) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-boto3 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(boto3) = %{epoch}:%{version}-%{release}

%description -n python3-boto3
Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK)
for Python, which allows Python developers to write software that makes
use of services like Amazon S3 and Amazon EC2.

%files -n python3-boto3
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
