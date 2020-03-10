%matplotlib inline
%config InlineBackend.figure_format = 'retina'

plt.figure(figsize=(15,4))
plt.title("342342")
plt.subplot(131) 
plt.plot(train_logger[0], label='Train loss')
plt.plot(val_logger[0], label='Val loss')
plt.legend(frameon=False)
plt.subplot(132) 
plt.plot(train_logger[1], label='Train acc1')
plt.plot(val_logger[1], label='Val acc1')
plt.legend(frameon=False)
plt.title('Radio',fontsize=18,color='r')
plt.subplot(133)
plt.plot(train_logger[2], label='Train acc5')
plt.plot(val_logger[2], label='Val acc5')
plt.legend(frameon=False)
plt.show()
