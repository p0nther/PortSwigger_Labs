

picoCTF – Super Serial Writeup

This writeup explains the Super Serial challenge from picoCTF in a clear, step-by-step way, focusing on why the flag appeared and how the vulnerability was exploited.


---

Overview

The challenge is based on a vulnerability called PHP Object Injection, which happens when user-controlled data is passed into the PHP function unserialize().
This vulnerability often leads to the ability to trigger magic methods in unexpected classes, allowing an attacker to execute arbitrary code such as reading files.

The application tracks user permissions using a serialized object stored in a cookie.


---

Application Behavior (Normal Flow)

The server expects a cookie named login that contains a serialized object of this class:

UserPermissions
Responsible for checking whether the user is logged in and whether they are an admin.


There is another class in the code:

access_log
Responsible for writing logs to a file.
This class contains a dangerous magic method:

public function __toString() {
    return file_get_contents($this->log_file);
}

This is the “gadget” that enables reading arbitrary files.


The server reads the cookie like this:

$perm = unserialize(base64_decode(urldecode($_COOKIE["login"])));

The expected object type is UserPermissions.


---

Attack Strategy

The attack goal is to force the server to deserialize a malicious object instead of the normal UserPermissions object, so that the magic method __toString() is executed to read the flag.

Step 1 – Build the Malicious Object

We use the vulnerable access_log class.

We create a serialized object where:

The class is access_log

The attribute log_file is overwritten with "../flag"


This ensures that when __toString() is called, it will execute:

file_get_contents("../flag");

and return the flag.

The crafted payload (before encoding) looks like:

O:10:"access_log":1:{s:8:"log_file";s:7:"../flag";}

After that, we URL-encode and Base64-encode it to create the final cookie value.


---

Step 2 – Trigger the Magic Method

In authentication.php, the application writes logs using something like:

$log->append_to_log("Logged in - User: " . $perm);

When PHP sees the expression:

"string" . $perm

it must convert $perm to a string.
Because $perm is now an access_log object, PHP automatically calls the magic method:

__toString()

This method reads the file specified in log_file, which we set to ../flag.
So the returned string is the flag itself, and the application prints it.


---

Why a Fatal Error Also Appears

After printing the flag, the script continues executing the original logic.
The code still assumes $perm is a UserPermissions object and tries calling a method like:

$perm->is_admin();

But this method does not exist in access_log.

PHP then throws a fatal error:

Call to undefined method access_log::is_admin()

This does not affect reading the flag — the flag is already printed before the crash.


---

Final Summary

1. The cookie is deserialized using unserialize().


2. We replaced the expected UserPermissions object with an access_log object.


3. During logging, PHP tried to cast the object to a string.


4. This triggered the magic method __toString().


5. __toString() read the file ../flag and returned its content.


6. The application printed the flag, then crashed because $perm wasn’t the expected class.




---

لو محتاج أضيف PoC جاهز، script Python للبناء التلقائي للـ payload، أو diagram بسيط يشرح الـ flow، قول لي وهنزودهم فورًا في نفس الـ README.
