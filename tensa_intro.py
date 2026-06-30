import tensorflow as tf

numbers = tf.constant([10,20,30])

print(numbers)

student_marks = tf.constant([
    [70,90],
    [90,60]
])
print(student_marks)

#Tensor operations
#sum
marks = tf.constant([70,80,90,50,60])

print(tf.reduce_sum(marks))

#Average
print(tf.reduce_mean(tf.cast(marks, tf.float32)))

#Return highest value
print(tf.reduce_max(marks))

#return lowest value
print(tf.reduce_min(marks))

#Product of all values
print(tf.reduce_prod(marks))

#index of the highest value
print(tf.argmax(marks))

#Index of the lowest value
print(tf.argmin(marks))
