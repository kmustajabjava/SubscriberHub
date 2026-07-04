from controllers.customer_controller import CustomerController


def main():

    controller = CustomerController()

    # controller.display_customers()

    controller.register_customer()


if __name__ == "__main__":

    main()