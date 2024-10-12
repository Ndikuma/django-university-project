from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import emoji

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='notes',null=False)

    def __str__(self):
        return self.title  
    


# User Profile Model (extended Django user with additional fields)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    friends = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

# Department Model
class Department(models.Model):
    name = models.CharField(max_length=255)
    building = models.CharField(max_length=255)
    head = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Student Model
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment_number = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    address = models.TextField()
    enrollment_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.enrollment_number})"

# Faculty Model
class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    date_of_joining = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.employee_id})"

# Course Model
class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    credits = models.IntegerField()
    faculty = models.ManyToManyField(Faculty, related_name='courses')

    def __str__(self):
        return f"{self.name} ({self.code})"

# Enrollment Model
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.IntegerField()
    date_enrolled = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.student} enrolled in {self.course}"

# Exam and Grade Models
class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    exam_date = models.DateField()
    exam_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.exam_type} for {self.course}"

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.student} - {self.grade} in {self.exam}"

# University Event Model
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=255)
    participants = models.ManyToManyField(Student, related_name='events')

    def __str__(self):
        return self.title

# Library Resource Model
class LibraryResource(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    category = models.CharField(max_length=100)
    available_copies = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author}"

# Attendance Model
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.student} - {self.status} on {self.date}"

# Chat Group Model
class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    members = models.ManyToManyField(UserProfile, related_name='chat_groups')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Chat Message Model
class Chat(models.Model):
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='received_messages', null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group_messages', null=True, blank=True)
    message_type = models.CharField(max_length=20, choices=[('text', 'Text'), ('voice', 'Voice'), ('file', 'File')])
    text_content = models.TextField(blank=True, null=True)
    file_content = models.FileField(upload_to='message_files/', blank=True, null=True)
    voice_content = models.FileField(upload_to='voice_messages/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.receiver:
            return f"Message from {self.sender.user.username} to {self.receiver.user.username} at {self.created_at}"
        else:
            return f"Group Message from {self.sender.user.username} in {self.group.name} at {self.created_at}"

    def save(self, *args, **kwargs):
        # Convert any emoji shortcode to an actual emoji
        if self.text_content:
            self.text_content = emoji.emojize(self.text_content, use_aliases=True)
        super().save(*args, **kwargs)

# Friend Request Model
class FriendRequest(models.Model):
    from_user = models.ForeignKey(UserProfile, related_name='sent_requests', on_delete=models.CASCADE)
    to_user = models.ForeignKey(UserProfile, related_name='received_requests', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Friend request from {self.from_user.user.username} to {self.to_user.user.username}"

    class Meta:
        unique_together = ('from_user', 'to_user')